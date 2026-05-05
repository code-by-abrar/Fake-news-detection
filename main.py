import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks
from database import Base, engine

from fastapi.responses import FileResponse 
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)

# Load environment variables
os.environ.pop("OPENAI_API_KEY", None)
load_dotenv()

app = FastAPI(title="Fake News Detector API")
# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request Model with Validation
class ClaimRequest(BaseModel):
    claim: str = Field(..., min_length=5, max_length=2000, description="The news claim to verify.")

# @app.get("/")
# async def read_index():
import os
from fastapi.responses import FileResponse

@app.get("/")
async def read_index():
    # Ye line check karti hai ke file waqai wahan mojood hai ya nahi
    file_path = os.path.join(os.getcwd(), "index.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "index.html file not found inside the container"}#     return FileResponse('index.html')





@app.post("/verify")
async def verify_news(request: ClaimRequest):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY missing in .env file"
        )

    try:
        # 1. Initialize Agents
        researcher, editor = create_agents()

        # 2. Create Tasks
        tasks = create_tasks(researcher, editor, request.claim)

        # 3. Create Crew
        crew = Crew(
            agents=[researcher, editor],
            tasks=tasks,
            process=Process.sequential,
            verbose=os.getenv("DEBUG", "False").lower() == "true",
        )

        # 4. Run Agents
        result = crew.kickoff()
        report_str = str(result)
        
        # Extract Truth Score for the gauge
        score_match = re.search(r"TRUTH SCORE:\s*(\d+)", report_str, re.IGNORECASE)
        truth_score = int(score_match.group(1)) if score_match else 50 # Default to 50 if not found

        return {
            "status": "success",
            "claim": request.claim,
            "report": report_str,
            "score": truth_score
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

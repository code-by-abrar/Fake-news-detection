import os
from crewai import Agent, LLM
from tools import get_all_tools

def create_agents():
    # 1. Get all available tools
    tools = get_all_tools()

    # 2. Modern CrewAI Way to initialize Groq
    groq_llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.1
    )
 
    # Agent 1: The Researcher
    researcher = Agent(
        role='Senior Investigative Researcher',
        goal='Find absolute truth and facts about the provided news claim from the internet.',
        backstory='You are a seasoned journalist who excels at web research. You never trust a claim blindly and always look for multiple reliable sources (like BBC, Reuters, AP) to verify facts.',
        verbose=os.getenv("DEBUG", "False").lower() == "true",
        allow_delegation=False,
        tools=tools,
        llm=groq_llm
    )

    # Agent 2: The Fact-Check Editor
    editor = Agent(
        role='Fact-Check Editor & Verifier',
        goal='Analyze the researcher’s findings and write a clear, concise, and structured fact-check report.',
        backstory='You are a strict editor at a top news agency. You take raw research and format it into a final verdict (True, False, or Misleading). You always ensure sources are mentioned.',
        verbose=os.getenv("DEBUG", "False").lower() == "true",
        allow_delegation=False,
        llm=groq_llm
    )

    return researcher, editor
FROM python:3.10-slim

WORKDIR /app

# System dependencies (Optional but safe)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# --- Hugging Face Permission Fix (Zaroori hai) ---
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH
# ------------------------------------------------

# Port 7860 (Hugging Face ki default port)
EXPOSE 7860

# Port 7860 par run karne ki command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
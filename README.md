# 📰 VeriFact AI — Multi-Agent Fake News & Misinformation Detection Engine

<div align="center">

[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF4B4B.svg?style=for-the-badge)](https://crewai.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?style=for-the-badge&logo=docker)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

**An autonomous multi-agent verification system powered by CrewAI that fact-checks news articles, assesses linguistic sentiment bias, and scores source credibility.**

</div>

---

## 📌 Overview

Misinformation spreads faster than truth. **VeriFact AI** addresses this challenge by deploying a specialized squad of autonomous AI agents working collaboratively to verify claims, corroborate sources, identify sensationalist clickbait, and issue comprehensive authenticity verdicts.

---

## 🤖 Multi-Agent Workflow (CrewAI)

```text
               ┌──────────────────────────────┐
               │    Submitted News Article    │
               └──────────────┬───────────────┘
                              │
                              ▼
               ┌──────────────────────────────┐
               │    Research & Fact Checker   │
               │  - Cross-references claims   │
               └──────────────┬───────────────┘
                              │
                              ▼
               ┌──────────────────────────────┐
               │    Linguistic Bias Auditor   │
               │  - Emotion & Clickbait score │
               └──────────────┬───────────────┘
                              │
                              ▼
               ┌──────────────────────────────┐
               │  Final Verdict Synthesizer   │
               │ - Truth Score (0 - 100%)     │
               └──────────────────────────────┘
```

---

## ⚡ Features

- **👥 Multi-Agent Collaboration**: Built with `crewai` assigning specific investigative personas.
- **📊 Authenticity Score**: Provides transparent, explained ratings (e.g. *True*, *Mostly False*, *Manipulated Context*).
- **🐳 Full Containerization**: One-click setup using `docker-compose.yml`.
- **💻 Web UI & REST API**: Interactive web frontend (`index.html`) backed by FastAPI endpoints.

---

## 🚀 Quick Start

### Using Docker:
```bash
docker-compose up --build
```
Access the dashboard at `http://localhost:8000`.

### Manual Local Setup:
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

🧠 Resume-Generator-Ai

Resume-Generator-Ai is a full-stack AI resume builder that collects structured professional data via a modern frontend and generates high-quality resumes using an LLM-powered backend.

🚧 Status: Actively under development (POC → Portfolio-grade project)

🎯 What This Project Does (High Level)

Collects schema-validated resume data from users (Frontend)

Sends clean JSON to an API-first AI backend

Uses LLM inference to generate professional resume content

Designed to scale into PDF/DOCX generation & deployment

🧩 System Architecture (Simplified)

Frontend (HTML / CSS / JS)
→ Structured JSON
→ FastAPI Backend
→ LLM Inference
→ Generated Resume Content

📂 Repository Structure
Resume-Generator-AI/
│
├── frontend/
│   └── README.md   # UI, form logic, JSON schema output
│
├── backend/
│   └── README.md   # FastAPI, schema validation, AI inference
│
└── README.md       # (You are here) Project overview & navigation


👉 For detailed setup and logic, refer to:

Frontend docs: /frontend/README.md

Backend docs: /backend/README.md

🛠 Tech Stack (At a Glance)

Frontend

HTML, CSS (Glassmorphism UI)

JavaScript (Dynamic forms, JSON generation)

Dark / Light mode support

Backend

Python 3.10+

FastAPI

Pydantic (schema-driven input)

LLM (LLaMA / OpenAI / local — pluggable)

🔁 Frontend ↔ Backend Contract

Frontend generates strict JSON

JSON must match backend schema.py

Backend rejects malformed input

Clean separation = scalable system

This makes the project:

Easier to debug

API-friendly

Production-ready by design

🔮 Planned Enhancements

Resume PDF / DOCX export

Multiple resume templates

OCR-based resume input

Authentication & user profiles

Dockerized deployment (cloud-ready)

🤝 Collaboration

Frontend: UI/UX, form logic, schema-aligned JSON

Backend: API design, AI inference, validation

Communication: REST API (JSON)

📌 Why This Repo Exists

Portfolio-grade AI project

Demonstrates system design + AI integration

Proof of concept for real-world AI services
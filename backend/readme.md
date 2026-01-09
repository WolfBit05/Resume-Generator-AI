# Resume Generator AI

An AI-powered resume generation backend that converts structured user inputs into a professionally formatted resume using LLM inference.  
Built as a modular, API-first service to easily integrate with any frontend (HTML/CSS/React).

---

## 🚀 Project Overview

This project focuses on the **AI inference and API layer** for resume generation.  
Frontend (HTML/CSS) is handled separately and communicates with this backend via HTTP requests.

Core goals:
- Clean schema-driven input (Pydantic)
- LLM-based resume content generation
- Easy integration with web or mobile frontends
- Scalable, production-style structure

---

## 🧠 Architecture (High Level)

Frontend (HTML/CSS)
|
| JSON (POST request)
v
FastAPI (app.py)
|
v
Inference Logic (inference.py)
|
v
LLM / Resume Template Logic


---

## 📂 Folder Structure

resume_generator_ai/
│
├── app.py # FastAPI entry point (API routes)
├── inference.py # Resume generation logic (AI inference)
├── schema.py # Pydantic models for input/output validation
├── requirements.txt
└── README.md


---

## 🧩 File Responsibilities

### `app.py`
- Creates FastAPI app
- Defines API endpoints (e.g., `/generate-resume`)
- Receives validated input from `schema.py`
- Calls inference functions from `inference.py`

### `schema.py`
- Defines structured input using **Pydantic**
- Ensures clean, validated data (no messy raw JSON)
- Acts as a contract between frontend & backend

### `inference.py`
- Core AI logic lives here
- Converts structured data → prompt → resume content
- Is independent of FastAPI (pure Python logic)

---

## 🔁 How Files Are Connected

- `app.py` **imports** schemas from `schema.py`
- `app.py` **imports and calls** functions from `inference.py`
- `inference.py` does **not** talk to FastAPI directly (clean separation)

Example flow:

POST request → app.py → schema validation → inference.py → response


---

## 📡 API Endpoint (Example)

**POST** `/generate-resume`

**Request Body (JSON):**
```json
{
  "name": "John Doe",
  "skills": ["Python", "Machine Learning"],
  "experience": "2 years in data science",
  "education": "MCA"
}

Response:

{
  "resume_text": "Generated professional resume content..."
}

🛠 Tech Stack

    Python 3.10+

    FastAPI

    Pydantic

    LLM (LLaMA / OpenAI / local model — pluggable)

🧪 Local Setup

pip install -r requirements.txt
uvicorn app:app --reload

API will be live at:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

🔮 Future Enhancements

    PDF / DOCX resume export

    Multiple resume templates

    OCR-based resume input

    User authentication

    Deployment using Docker + cloud

🤝 Collaboration

    Backend / AI: Resume Generator AI

    Frontend: HTML/CSS handled separately

    Communication via REST API

📌 Status

🚧 Proof of Concept (POC)
Designed for portfolio, learning, and future production scaling.


---

### Quick self-check (important, kanna):
- If someone deletes `inference.py`, **FastAPI should still run** → correct design.
- If frontend changes, backend should **not** change → API-first mindset.

**Next step:**  
Want me to add **real FastAPI route + inference stub code** matching this README so everything aligns 1:1?


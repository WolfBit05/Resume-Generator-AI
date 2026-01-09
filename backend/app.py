from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from inference import generate_resume
from schema import ResumeAIInput  # your pydantic schema file

app = FastAPI(title="Resume AI API")


# ---------- Inference-only config ----------

class ResumeConstraints(BaseModel):
    resume_length: Literal["1_page", "2_pages"] = "1_page"
    region: Literal["India", "Global"] = "India"
    tone: Literal["Formal", "Neutral"] = "Formal"


class ResumeRequest(BaseModel):
    role_target: str
    constraints: ResumeConstraints
    user_data: ResumeAIInput


# ---------- API Endpoint ----------

@app.post("/generate-resume")
def generate_resume_api(request: ResumeRequest):
    user_profile = {
        "role_target": request.role_target,
        "constraints": request.constraints.model_dump(),
        **request.user_data.model_dump()
    }

    resume_text, = generate_resume(user_profile)

    return {
        "status": "success",
        "resume_markdown": resume_text
    }

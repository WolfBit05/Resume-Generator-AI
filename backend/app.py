from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Literal
from services.inference import generate_resume
from services.evaluation_engine import evaluate_resume
from services.pipeline import run_resume_pipeline
from fastapi import HTTPException
from schema import ResumeAIInput  # your existing Pydantic schema

app = FastAPI(title="Resume AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        "user_data": request.user_data.model_dump()
    }

    try:
        result = run_resume_pipeline(user_profile)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return result





"""@app.post("/generate-resume")
async def generate_resume_api(request: Resum    eRequest):
    try:
        user_profile = {
            "role_target": request.role_target,
            "constraints": request.constraints.model_dump(),
            **request.user_data.model_dump()
        }

        # 🔎 Debug: return what backend received
        resume_text = f"""
'''# Resume Debug

Name: {user_profile['personal_info']['full_name']}
Email: {user_profile['personal_info']['email']}
Target Role: {user_profile['role_target']}'''
"""

        return {
            "status": "success",
            "resume_markdown": resume_text
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}"""





'''from fastapi import FastAPI
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

    resume_text = generate_resume(user_profile)

    return {
        "status": "success",
        "resume_markdown": resume_text
    }'''

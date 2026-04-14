from services.inference import generate_resume
from services.evaluation_engine import evaluate_resume
from services.refinement import refine_resume   # 👈 add this

def run_resume_pipeline(user_profile: dict):
    resume_text = generate_resume(user_profile)

    evaluation = evaluate_resume(resume_text)

    improved_resume = refine_resume(resume_text, evaluation)  # 👈 add this

    return {
        "status": "success",
        "resume_markdown": improved_resume,
        "evaluation": evaluation
    }
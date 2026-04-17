from services.inference import generate_resume
from services.evaluation_engine import evaluate_resume
from services.refinement import refine_resume

def run_resume_pipeline(user_profile: dict):
    resume_text = generate_resume(user_profile)
    
    initial_evaluation = evaluate_resume(resume_text)
    improved_resume = refine_resume(resume_text, initial_evaluation)
    
    # re-evaluate the final output
    final_evaluation = evaluate_resume(improved_resume)

    return {
        "status": "success",
        "resume_markdown": improved_resume,
        "evaluation": final_evaluation,
        "score_delta": round(
            final_evaluation["overall_score"] - initial_evaluation["overall_score"], 2
        )
    }
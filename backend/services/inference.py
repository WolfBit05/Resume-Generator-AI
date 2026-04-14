def generate_resume(user_profile: dict) -> str:
    data = user_profile.get("user_data", {})

    resume_lines = []

    # Header
    pi = data.get("personal_info", {})
    resume_lines.append(f"# {pi.get('full_name')}")
    resume_lines.append(f"{pi.get('email')} | {pi.get('phone_number')}\n")

    # Objective 
    resume_lines.append("## Objective")
    resume_lines.append(f"- {data.get('objective')}\n")

    # Skills
    resume_lines.append("## Skills")
    for group in data.get("skills", []):
        skill_list = ", ".join(group.get("skills", []))
        resume_lines.append(f"- {group.get('skill_type')}: {skill_list}")
    resume_lines.append("")

    # Experience
    resume_lines.append("## Experience")
    for exp in data.get("experience", []):
        resume_lines.append(f"### {exp.get('role')} - {exp.get('organization')}")
        for resp in exp.get("responsibilities", []):
            resume_lines.append(f"- {resp}")
    resume_lines.append("")

    # Projects
    resume_lines.append("## Projects")
    for proj in data.get("projects", []):
        resume_lines.append(f"### {proj.get('title')}")
        resume_lines.append(f"- {proj.get('description')}")
        techs = ", ".join(proj.get("technologies", []))
        if techs:
            resume_lines.append(f"- Technologies: {techs}")
    resume_lines.append("")

    # Education
    resume_lines.append("## Education")
    for edu in data.get("education", []):
        resume_lines.append(
            f"- {edu.get('degree')}, {edu.get('institution')} ({edu.get('year')})"
        )

    return "\n".join(resume_lines)


# saveral days old code
'''from settings import settings
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import json
from huggingface_hub import login
from huggingface_hub import whoami

login(token=settings.hf_token)
print(whoami())

MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16,
    device_map="auto"
)

SYSTEM_PROMPT = """
You are a professional ATS-optimized resume generator.

Non-negotiable rules:
- Use ONLY the data explicitly provided by the user.
- Do NOT invent companies, roles, skills, metrics, grades, or certifications.
- Do NOT add soft skills unless supported by evidence.
- Keep content concise, factual, and impact-driven.
- Use standard resume sections only.
- If a section has insufficient data, omit it completely.

Formatting rules:
- No first-person language.
- Bullet points only for experience and projects.
- Each bullet must follow: Action verb + What + Impact/Outcome.
- Optimize for ATS keyword parsing.

Priority order:
Accuracy > Relevance > Brevity
"""

def build_user_prompt(user_profile: dict) -> str:
    return f"""
Generate a professional resume.

Target Role:
{user_profile["role_target"]}

Constraints:
- Resume length: {user_profile["constraints"]["resume_length"]}
- Region: {user_profile["constraints"]["region"]}
- Tone: {user_profile["constraints"]["tone"]}

User Data (JSON):
{json.dumps(user_profile, indent=2)}

Instructions:
- Align content to target role.
- Be ATS-friendly.
- Use markdown formatting.
"""

def generate_resume(user_profile: dict) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": build_user_prompt(user_profile)}
    ]

    input_ids = tokenizer.apply_chat_template(
        messages,
        return_tensors="pt"
    ).to(model.device)

    output = model.generate(
        input_ids,
        max_new_tokens=900,
        temperature=0.25,
        top_p=0.9
    )

    return tokenizer.decode(output[0], skip_special_tokens=True)'''

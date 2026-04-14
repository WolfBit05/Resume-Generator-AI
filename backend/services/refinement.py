from services.model_loader import tokenizer, model
import re

WEAK_STARTS = {
    "worked on": "Developed",
    "helped": "Assisted in",
    "assisted": "Assisted in",
    "involved in": "Contributed to"
}

def strengthen_bullet(text: str):
    text = text.strip()

    lower = text.lower()

    for weak, strong in WEAK_STARTS.items():
        if lower.startswith(weak):
            text = strong + text[len(weak):]
            break

    # Capitalize first letter
    return text[:1].upper() + text[1:]

def rule_based_refinement(resume_text: str):
    lines = resume_text.split("\n")
    new_lines = []

    for line in lines:
        if line.strip().startswith("- "):
            bullet = line.strip()[2:]
            improved = strengthen_bullet(bullet)
            new_lines.append(f"- {improved}")
        else:
            new_lines.append(line)

    return "\n".join(new_lines)


from services.model_loader import tokenizer, model

def refine_resume(resume_text: str, evaluation: dict):

    print("🔥 HYBRID REFINEMENT RUNNING")

    # 👉 Step 1: rule-based improvement
    rule_improved = rule_based_refinement(resume_text)

    feedback = "\n".join(evaluation.get("recommendations", []))

    # 👉 Step 2: LLM polishing (optional but kept)
    prompt = f"""
Improve the clarity and professionalism of this resume.

Keep same meaning. Do not add new information.

Resume:
{rule_improved}

Improved Resume:
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    ).to("cpu")

    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        num_beams=4,
        early_stopping=True
    )

    final_output = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # fallback if model fails
    if len(final_output) < 50:
        return rule_improved

    return final_output
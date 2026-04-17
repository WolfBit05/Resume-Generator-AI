import requests
import re
from settings import settings

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama-3.1-8b-instant"

WEAK_STARTS = {
    "worked on": "Developed",
    "helped": "Assisted in",
    "assisted": "Assisted in",
    "involved in": "Contributed to",
    "responsible for": "Managed",
}

def strengthen_bullet(text: str) -> str:
    text = text.strip()
    lower = text.lower()
    for weak, strong in WEAK_STARTS.items():
        if lower.startswith(weak):
            text = strong + text[len(weak):]
            break
    return text[:1].upper() + text[1:]

def rule_based_refinement(resume_text: str) -> str:
    lines = resume_text.split("\n")
    return "\n".join(
        f"- {strengthen_bullet(line.strip()[2:])}"
        if line.strip().startswith("- ") else line
        for line in lines
    )

def build_refinement_prompt(resume_text: str, recommendations: list) -> str:
    feedback = "\n".join(f"- {r}" for r in recommendations) if recommendations else "None"
    return f"""You are a professional resume editor. Improve the resume below.

STRICT RULES — violations will reject your output:
- Do NOT invent any numbers, percentages, or metrics not present in the input.
- Do NOT add new companies, tools, skills, or achievements.
- Do NOT change section headings or structure.
- Only improve language: replace weak verbs, tighten sentences, remove first-person.
- If a bullet has no metrics, do NOT add metrics. Leave it metric-free.

Feedback to address:
{feedback}

Resume:
{resume_text}

Return only the improved resume. No explanations, no preamble."""

def extract_numbers(text: str) -> set:
    return set(re.findall(r'\b\d+\.?\d*%?\b', text))

def validate_llm_output(original: str, llm_output: str) -> bool:
    original_numbers = extract_numbers(original)
    llm_numbers = extract_numbers(llm_output)

    # check 1: numbers from original must still be present
    missing = original_numbers - llm_numbers
    if missing:
        print(f"⚠ Missing numbers: {missing}")
        return False

    # check 2: LLM must not have added new numbers
    added = llm_numbers - original_numbers
    if added:
        print(f"⚠ Hallucinated numbers: {added}")
        return False

    return True

def refine_with_groq(prompt: str) -> str | None:
    try:
        response = requests.post(
            GROQ_URL,
            headers={
                "Authorization": f"Bearer {settings.groq_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
                "max_tokens": 600
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"⚠ Groq failed: {e}")
        return None

def refine_resume(resume_text: str, evaluation: dict) -> str:
    rule_improved = rule_based_refinement(resume_text)

    score = evaluation.get("overall_score", 100)
    recommendations = evaluation.get("recommendations", [])

    if score >= 75 and not recommendations:
        print("✓ Score above threshold, skipping LLM.")
        return rule_improved

    prompt = build_refinement_prompt(rule_improved, recommendations)
    llm_output = refine_with_groq(prompt)

    if llm_output and len(llm_output) > len(resume_text) * 0.5:
        if validate_llm_output(resume_text, llm_output):
            print("✅ Using Groq output.")
            return llm_output

    print("⚠ Falling back to rule-based.")
    return rule_improved
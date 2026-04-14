import re

STRONG_VERBS = [
    "built", "developed", "engineered", "optimized",
    "implemented", "designed", "automated",
    "improved", "increased", "reduced", "deployed"
]

WEAK_VERBS = [
    "worked on", "responsible for", "helped",
    "assisted", "involved in"
]

def extract_bullets(markdown: str):
    return re.findall(r"^- (.+)", markdown, re.MULTILINE)

def evaluate_resume(markdown: str):
    bullets = extract_bullets(markdown)
    total = len(bullets)

    if total == 0:
        return {"overall_score": 0, "error": "No bullets found"}

    bullets_with_numbers = sum(
        bool(re.search(r"\b\d+%?|\$\d+", b)) for b in bullets
    )
    strong_verb_hits = sum(
    any(v in b.lower().split()[:2] for v in STRONG_VERBS)
    for b in bullets
    )
    passive_hits = sum(
        " was " in b.lower() or " were " in b.lower()
        for b in bullets
    )

    weak_hits = sum(
    any(v in b.lower() for v in WEAK_VERBS)
    for b in bullets
    )

    quant_ratio = bullets_with_numbers / total
    impact_density = strong_verb_hits / total
    passive_ratio = passive_hits / total

    overall = (
        30 * quant_ratio +
        30 * impact_density +
        20 * (1 - passive_ratio) +
        20 * min(total / 10, 1) -
        20 * (weak_hits / total)
    )

    overall = max(0, min(100, overall))

    recommendations = []

    if quant_ratio < 0.5:
        recommendations.append("Increase measurable impact (add metrics, % improvements).")
    if impact_density < 0.6:
        recommendations.append("Start bullets with strong action verbs.")
    if passive_ratio > 0.2:
        recommendations.append("Reduce passive voice usage.")
    if weak_hits > 0:
        recommendations.append("Avoid weak phrases like 'worked on', 'assisted'.")

    return {
        "overall_score": round(overall, 2),
        "quantification_ratio": round(quant_ratio, 2),
        "impact_density": round(impact_density, 2),
        "passive_voice_ratio": round(passive_ratio, 2),
        "bullet_count": total,
        "recommendations": recommendations
    }
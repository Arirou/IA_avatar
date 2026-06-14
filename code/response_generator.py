import json
import requests


def generate_response(message, analysis, history, avatar_state, dialogue_state):

    tone_instruction = ""

    emotion = analysis.get("emotion", "neutral")

    if emotion == "sad":
        tone_instruction = "réponds de façon douce et humaine"
    elif emotion == "angry":
        tone_instruction = "réponds calmement sans confrontation"
    elif emotion == "happy":
        tone_instruction = "réponds de façon positive et simple"
    elif analysis.get("urgency") == "high":
        tone_instruction = "réponds très court et direct"
    else:
        tone_instruction = "réponds naturellement"

    prompt = f"""
Tu es un avatar conversationnel social.

Tu n'es PAS un assistant.

STYLE IMPORTANT :
- phrases courtes
- humain naturel
- pas de phrases robotiques
- pas de formules d'assistant

CONSIGNE :
{tone_instruction}

═══════════════════════
RÈGLES STRICTES (IMPORTANT)
═══════════════════════

EXPRESSIONS AUTORISÉES :
neutre, triste, souriant, calme, empathique, concentré

GESTES AUTORISÉS :
attente, ouverture, apaisement, reconfort, rapide

TON AUTORISÉ :
neutre, doux, calme, direct, chaleureux

═══════════════════════
CONTEXTE
═══════════════════════

Analyse :
{analysis}

Historique :
{json.dumps(history[-6:], ensure_ascii=False)}

Message :
{message}

═══════════════════════
FORMAT OBLIGATOIRE
═══════════════════════

Réponds UNIQUEMENT en JSON valide :

{{
  "response": "réponse naturelle courte",
  "expression": "neutre",
  "gesture": "attente",
  "tone": "neutre"
}}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    raw = response.json().get("response", "")

    start = raw.find("{")
    end = raw.rfind("}") + 1

    if start == -1 or end == -1:
        return {
            "response": raw,
            "expression": "neutre",
            "gesture": "attente",
            "tone": "neutre"
        }

    clean = raw[start:end]

    try:
        data = json.loads(clean)

        # sécurité anti valeurs inventées
        allowed_expr = ["neutre", "triste", "souriant", "calme", "empathique", "concentré"]
        allowed_gesture = ["attente", "ouverture", "apaisement", "reconfort", "rapide"]
        allowed_tone = ["neutre", "doux", "calme", "direct", "chaleureux"]

        if data.get("expression") not in allowed_expr:
            data["expression"] = "neutre"

        if data.get("gesture") not in allowed_gesture:
            data["gesture"] = "attente"

        if data.get("tone") not in allowed_tone:
            data["tone"] = "neutre"

        return data

    except:
        return {
            "response": raw,
            "expression": "neutre",
            "gesture": "attente",
            "tone": "neutre"
        }
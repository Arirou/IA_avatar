import json
import requests


def analyze_with_llm(message):

    prompt = f"""
Analyse le message suivant.

Message :
"{message}"

Retourne UNIQUEMENT un JSON valide.

Format :

{{
    "emotion": "neutral",
    "speech_act": [],
    "politeness": "neutral",
    "urgency": "low"
}}

Valeurs possibles :

emotion :
- sad
- angry
- happy
- stress
- neutral

speech_act :
- assertive
- directive
- expressive
- commissive
- indirect_request

politeness :
- polite
- direct
- neutral

urgency :
- high
- low

Aucune explication.
Uniquement le JSON.
"""

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        result = response.json()["response"].strip()

        start = result.find("{")
        end = result.rfind("}") + 1

        if start != -1 and end != -1:
            result = result[start:end]

        return json.loads(result)

    except Exception as e:

        print("LLM ANALYSIS ERROR :", e)

        return {
            "emotion": "neutral",
            "speech_act": [],
            "politeness": "neutral",
            "urgency": "low"
        }
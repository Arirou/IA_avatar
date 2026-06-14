def analyze_social(message):
    m = message.lower()

    result = {
        "emotion": "neutral",
        "valence": 0,
        "politeness": "neutral",
        "speech_act": "assertive",
        "urgency": "low"
    }

    # =====================
    # EMOTIONS
    # =====================
    if any(w in m for w in ["triste", "déprimé", "fatigué", "mal"]):
        result["emotion"] = "sad"
        result["valence"] = -1

    elif any(w in m for w in ["énervé", "marre", "dégage", "nul"]):
        result["emotion"] = "angry"
        result["valence"] = -1

    elif any(w in m for w in ["content", "heureux", "super", "génial"]):
        result["emotion"] = "happy"
        result["valence"] = 1

    # =====================
    # POLITESSE
    # =====================
    if any(w in m for w in ["s'il te plaît", "s'il vous plaît", "pourrais-tu", "pourriez-vous", "aurais-tu", "serait-il possible"]):
        result["politeness"] = "polite"

    elif any(w in m for w in ["dépêche", "vite", "maintenant", "tout de suite"]):
        result["politeness"] = "urgent"

    elif any(w in m for w in ["ferme", "donne", "fais", "arrête"]):
        result["politeness"] = "direct"

    # =====================
    # ACTES DE LANGAGE (SEARLE)
    # =====================
    if "?" in message:
        result["speech_act"] = "directive"

    if any(w in m for w in ["je veux", "je vais", "je peux"]):
        result["speech_act"] = "assertive"

    if any(w in m for w in ["promets", "je promets"]):
        result["speech_act"] = "commissive"

    if any(w in m for w in ["merci", "bravo", "désolé", "pardon"]):
        result["speech_act"] = "expressive"

    # =====================
    # URGENCE
    # =====================
    if any(w in m for w in ["vite", "urgent", "rapidement", "dépêche"]):
        result["urgency"] = "high"

    return result
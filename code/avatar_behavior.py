def update_avatar_state(analysis):

    emotion = analysis.get("emotion", "neutral")

    state = {
        "expression": "neutre",
        "gesture": "attente",
        "tone": "neutre"
    }

    if emotion == "sad":
        state["expression"] = "triste"
        state["gesture"] = "reconfort"
        state["tone"] = "douceur"

    elif emotion == "angry":
        state["expression"] = "calme"
        state["gesture"] = "apaisement"
        state["tone"] = "posé"

    elif emotion == "happy":
        state["expression"] = "souriant"
        state["gesture"] = "ouverture"
        state["tone"] = "positif"

    elif emotion == "stress":
        state["expression"] = "alert"
        state["gesture"] = "rapide"
        state["tone"] = "direct"

    return state
def analyze_message(message):

    m = message.lower()

    score = {
        "sad": 0,
        "angry": 0,
        "happy": 0
    }

    if any(w in m for w in ["triste", "vide", "seul", "j'en peux plus", "ça va pas"]):
        score["sad"] += 3

    if any(w in m for w in ["énervé", "marre", "nul", "dégage"]):
        score["angry"] += 3

    if any(w in m for w in ["content", "super", "génial", "incroyable"]):
        score["happy"] += 3

    emotion = max(score, key=score.get)

    if score[emotion] == 0:
        emotion = "neutral"

    speech_act = []

    if "?" in message:
        speech_act.append("directive")

    if len(speech_act) == 0:
        speech_act = ["assertive"]

    return {
        "emotion": emotion,
        "speech_act": speech_act,
        "urgency": "low",
        "intensity": max(score.values()) / 5
    }
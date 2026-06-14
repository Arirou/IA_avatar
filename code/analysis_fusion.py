def fuse_analysis(nlp, llm):

    result = {}

    # emotion
    result["emotion"] = llm["emotion"] if llm["emotion"] != "neutral" else nlp["emotion"]

    # speech act fusion propre
    speech = []
    speech.extend(nlp.get("speech_act", []))
    speech.extend(llm.get("speech_act", []))

    if result["emotion"] in ["sad", "angry", "happy"]:
        speech.append("expressive")

    result["speech_act"] = list(set(speech))

    # politesse
    result["politeness"] = llm["politeness"] if llm.get("politeness") != "neutral" else nlp["politeness"]

    result["urgency"] = llm.get("urgency", "low")

    result["intensity"] = nlp.get("intensity", 0.5)

    return result
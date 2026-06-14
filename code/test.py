import requests
import json
import time

URL = "http://127.0.0.1:8000/chat"

tests = {
    "TRISTESSE": [
        "je me sens pas bien",
        "j'en peux plus",
        "je me sens seul",
        "tout va mal en ce moment"
    ],

    "COLÈRE": [
        "tu réponds n'importe quoi",
        "dépêche-toi !",
        "c'est nul",
        "j'en ai marre"
    ],

    "JOIE": [
        "trop bien !!",
        "je suis content",
        "c'est génial",
        "incroyable merci"
    ],

    "URGENCE": [
        "vite réponds",
        "c'est urgent",
        "dépêche-toi stp",
        "réponds maintenant"
    ],

    "POLITESSE": [
        "est-ce que tu pourrais m'aider ?",
        "s'il te plaît aide-moi",
        "merci beaucoup",
        "excuse-moi"
    ],

    "INDIRECT": [
        "j'ai soif",
        "il fait froid ici",
        "la porte est ouverte",
        "j'arrive pas à voir"
    ]
}


def send_message(msg):
    try:
        r = requests.post(URL, json={"message": msg})
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def run_tests():
    for category, phrases in tests.items():
        print("\n" + "=" * 60)
        print(f"🧪 CATEGORIE : {category}")
        print("=" * 60)

        for p in phrases:
            print(f"\n👉 USER: {p}")

            res = send_message(p)

            if "error" in res:
                print("❌ ERROR:", res["error"])
                continue

            avatar = res.get("avatar", {})
            analysis = res.get("analysis", {})

            print("🤖 RESPONSE:", res.get("response"))
            print(f"🎭 EMOTION: {analysis.get('emotion')}")
            print(f"🙂 EXPRESSION: {avatar.get('expression')}")
            print(f"🗣️ TONE: {avatar.get('tone')}")
            print(f"📌 GESTURE: {avatar.get('gesture')}")

            time.sleep(0.5)


if __name__ == "__main__":
    run_tests()
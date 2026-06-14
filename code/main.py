from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from response_generator import generate_response
from nlp_analyzer import analyze_message
from conversation_memory import add_message, get_history
from avatar_behavior import update_avatar_state

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    add_message("user", request.message)

    analysis = analyze_message(request.message)
    avatar_state = update_avatar_state(analysis)
    history = get_history()

    result = generate_response(
        message=request.message,
        analysis=analysis,
        history=history,
        avatar_state=avatar_state,
        dialogue_state={}
    )

    response_text = result.get("response")

    if response_text is None:
        response_text = "..."

    avatar = {
        "expression": result.get("expression", "neutre"),
        "gesture": result.get("gesture", "attente"),
        "tone": result.get("tone", "neutre")
    }

    add_message("avatar", response_text)

    return {
        "response": response_text,
        "avatar": avatar,
        "analysis": analysis
    }
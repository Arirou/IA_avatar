async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();

    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        console.log("DATA:", data);

        // =========================
        // IMPORTANT FIX ICI
        // =========================
        addMessage(data.response, "bot");

        updateAvatar(data.avatar);
        updateAnalysis(data.analysis);

    } catch (error) {
        console.error(error);
        addMessage("Erreur serveur", "bot");
    }
}


function addMessage(text, type) {
    const messages = document.getElementById("messages");
    const div = document.createElement("div");

    div.className = `message ${type}`;
    div.textContent = text;

    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
}


function updateAvatar(avatar) {
    const avatarDiv = document.getElementById("avatar");

    if (!avatar) return;

    const exp = avatar.expression;

    if (exp === "souriant") avatarDiv.textContent = "😊";
    else if (exp === "calme") avatarDiv.textContent = "😐";
    else if (exp === "empathique") avatarDiv.textContent = "🥺";
    else if (exp === "concentré") avatarDiv.textContent = "🤔";
    else avatarDiv.textContent = "🙂";

    document.getElementById("expression").textContent = `Expression : ${avatar.expression}`;
    document.getElementById("gesture").textContent = `Geste : ${avatar.gesture}`;
    document.getElementById("tone").textContent = `Ton : ${avatar.tone}`;
}


function updateAnalysis(analysis) {
    document.getElementById("analysis").textContent =
        JSON.stringify(analysis, null, 4);
}
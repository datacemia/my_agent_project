
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from agents import Runner
from agent import my_agent
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

html_page = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>My AI Agent</title>
</head>
<body>
    <h1>Mon Agent IA</h1>
    <input type="text" id="message" placeholder="Écris ton message ici" style="width:300px;">
    <button onclick="sendMessage()">Envoyer</button>
    <p><strong>Réponse :</strong></p>
    <div id="response"></div>

    <script>
        async function sendMessage() {
            const message = document.getElementById("message").value;

            const res = await fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message })
            });

            const data = await res.json();
            document.getElementById("response").innerText = data.reply;
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return html_page

@app.post("/chat")
async def chat(request: ChatRequest):
    result = await Runner.run(my_agent, request.message)
    return {"reply": result.final_output}
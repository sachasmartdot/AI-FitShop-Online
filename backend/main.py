from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from fit_engine import recommend_size
# pour passe en prod cette version est mieux
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "products.json")) as f:
    products = json.load(f)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load products
#with open("products.json") as f:
#    products = json.load(f)


# ----------- ROUTES -----------

@app.get("/products")
def get_products():
    return products


@app.post("/recommend")
def recommend(data: dict):
    foot_length = data.get("foot_length")
    product = data.get("product")

    size, confidence = recommend_size(foot_length, product)

    return {
        "recommended_size": size,
        "confidence": confidence
    }


# ----------- CHAT AGENT -----------

def agent_reply(message):
    msg = message.lower()

    if "cadeau" in msg:
        return "C est pour qui ce cadeau ?"

    if "fille" in msg:
        return "D accord. Quel age environ et quel style ?"

    if "18" in msg:
        return "Bonne idee. Je vous propose des sneakers tendance. Connaissez vous sa pointure ou la longueur de son pied ?"

    if "pointure" in msg or "taille" in msg:
        return "Si vous avez la longueur du pied en cm je peux vous recommander une taille precise."

    return "Bonjour. Je suis votre assistant SachaSmart. Dites moi ce que vous cherchez."


@app.post("/chat")
def chat(data: dict):
    message = data.get("message")
    reply = agent_reply(message)

    return {"reply": reply}

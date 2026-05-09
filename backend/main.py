from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from fit_engine import recommend_size

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Charger produits
with open("products.json") as f:
    products = json.load(f)

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

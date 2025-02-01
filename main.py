from fastapi import FastAPI, Depends, HTTPException, Query
import requests
from typing import List, Optional
from pydantic import BaseModel
from fastapi.testclient import TestClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Crypto Market API", version="1.0")

COINGECKO_API_URL = os.getenv("COINGECKO_API_URL")
AVAILABLE_API_KEYS =  os.getenv("AVAILABLE_API_KEYS", "").split(",")

def authenticate(api_key: str = Query(...)):
    if api_key not in AVAILABLE_API_KEYS:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True

class Coin(BaseModel):
    id: str
    name: str
    symbol: str
    current_price: Optional[float] = None

class Category(BaseModel):
    id: str
    name: str


@app.get("/coins", response_model=List[Coin])
def list_coins(
    page_num: int = 1, per_page: int = 10, auth: bool = Depends(authenticate)
):
    response = requests.get(f"{COINGECKO_API_URL}/coins/markets", 
                            params={"vs_currency": "cad"})
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch data")
    coins = response.json()
    paginated_data = coins[(page_num - 1) * per_page : page_num * per_page]
    return paginated_data

@app.get("/categories", response_model=List[Category])
def list_categories(
    page_num: int = 1, per_page: int = 10, auth: bool = Depends(authenticate)
):
    response = requests.get(f"{COINGECKO_API_URL}/coins/categories")
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch categories")
    categories = response.json()
    paginated_data = categories[(page_num - 1) * per_page : page_num * per_page]
    return paginated_data

@app.get("/coin/{coin_id}", response_model=Coin)
def get_coin(coin_id: str, auth: bool = Depends(authenticate)):
    response = requests.get(f"{COINGECKO_API_URL}/coins/{coin_id}", params={"localization": "false"})
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Coin not found")
    resonse_data = response.json()
    current_price = resonse_data.get("market_data", {}).get("current_price", {}).get("cad")
    coin = Coin(**resonse_data, current_price=current_price)
    return coin

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0"}

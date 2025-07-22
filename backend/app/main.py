from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os
from app.mock.card_mock import mock_cards, Card
from uuid import UUID

load_dotenv()  # Загружаем .env

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"message": "Hello, FastAPI!"}

@app.get("/cards", response_model=list[Card])
def get_cards():
    return mock_cards

@app.get("/cards/{card_id}", response_model=Card)
def get_card(card_id: UUID):
    for card in mock_cards:
        if card.id == card_id:
            return card
    raise HTTPException(status_code=404, detail="Карточка не найдена")

@app.post("/cards", response_model=Card)
def create_card(card: Card):
    mock_cards.append(card)
    return card

@app.put("/cards/{card_id}", response_model=Card)
def update_card(card_id: UUID, card_data: Card):
    for idx, card in enumerate(mock_cards):
        if card.id == card_id:
            mock_cards[idx] = card_data
            return card_data
    raise HTTPException(status_code=404, detail="Карточка не найдена")

@app.delete("/cards/{card_id}")
def delete_card(card_id: UUID):
    for idx, card in enumerate(mock_cards):
        if card.id == card_id:
            del mock_cards[idx]
            # return {"detail": "Карточка удалена"} не знаю нужно такое сообщение или нет
    raise HTTPException(status_code=404, detail="Карточка не найдена")

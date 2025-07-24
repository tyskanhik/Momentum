from fastapi import APIRouter, HTTPException
from app.mocks.card_mock import mock_cards
from app.models.models import Card
from uuid import UUID

router = APIRouter()

@router.get("/", response_model=list[Card])
def get_cards():
    return mock_cards

@router.get("/{card_id}", response_model=Card)
def get_card(card_id: UUID):
    for card in mock_cards:
        if card.id == card_id:
            return card
    raise HTTPException(status_code=404, detail="Карточка не найдена")

@router.post("/", response_model=Card)
def create_card(card: Card):
    mock_cards.append(card)
    return card

@router.put("/{card_id}", response_model=Card)
def update_card(card_id: UUID, card_data: Card):
    for idx, card in enumerate(mock_cards):
        if card.id == card_id:
            mock_cards[idx] = card_data
            return card_data
    raise HTTPException(status_code=404, detail="Карточка не найдена")

@router.delete("/{card_id}", status_code=200) # пока оставлю этот, потом можно поменять на 204
def delete_card(card_id: UUID):
    for idx, card in enumerate(mock_cards):
        if card.id == card_id:
            del mock_cards[idx]
            return {"detail": "Карточка удалена"}
    raise HTTPException(status_code=404, detail="Карточка не найдена")
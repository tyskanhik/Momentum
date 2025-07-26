from fastapi import APIRouter, HTTPException
from app.mocks.user_mock import mock_users
from app.models.models import User
from uuid import UUID

router = APIRouter()

@router.get("/", response_model=list[User])
def get_users():
    return mock_users

@router.get("/{user_id}", response_model=User)
def get_user(user_id: UUID):
    for user in mock_users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Пользователь не найден")
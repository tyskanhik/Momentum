from datetime import datetime
from uuid import uuid4
from app.mock.user_mock import mock_users
from app.models.models import Card, CardUser

mock_card_users = [
    CardUser(id=user.id, nickname=user.nickname, avatar=user.avatar) for user in mock_users
]

mock_cards = [
    Card(
        id=uuid4(),
        name="Закат в горах",
        description="Фото с похода в Альпы",
        link="http://localhost:8000/static/media/1.jpg",
        owner=mock_card_users[0],
        likes=[mock_card_users[1]],
        createdAt=datetime(2025, 6, 5, 15, 0, 0)
    ),
    Card(
        id=uuid4(),
        name="Морское побережье",
        description="Отдых на Бали",
        link="http://localhost:8000/static/media/2.jpg",
        owner=mock_card_users[1],
        likes=[mock_card_users[0],mock_card_users[2]],
        createdAt=datetime(2025, 6, 6, 11, 20, 0)
    ),
    Card(
        id=uuid4(),
        name="Городская архитектура",
        link="http://localhost:8000/static/media/3.jpg",
        owner=mock_card_users[2],
        likes=[],
        createdAt=datetime(2025, 6, 7, 14, 45, 0)
    ),
    Card(
        id=uuid4(),
        name="Лесной водопад",
        description="Поход в Карелию",
        link="http://localhost:8000/static/media/4.jpg",
        owner=mock_card_users[0],
        likes=[mock_card_users[2]],
        createdAt=datetime(2025, 6, 8, 9, 10, 0)
    ),
    Card(
        id=uuid4(),
        name="Кофе утром",
        link="http://localhost:8000/static/media/5.jpg",
        owner=mock_card_users[1],
        likes=[],
        createdAt=datetime(2025, 6, 9, 8, 0, 0)
    ),
]
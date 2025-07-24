from datetime import datetime
from app.models.models import User

mock_users = [
    User(
        id="1",
        name="Иван Петров",
        nickname="ivanpetrov",
        avatar="/static/avatar/avtr_1.jpg",
        following=["2"],
        followers=["2", "3"],
        createdAt=datetime(2025, 7, 1, 10, 0, 0)
    ),
    User(
        id="2",
        name="Мария Иванова",
        nickname="mariaivanova",
        avatar="/static/avatar/avtr_2.jpg",
        following=["1"],
        followers=["1"],
        createdAt=datetime(2025, 7, 2, 12, 30, 0)
    ),
    User(
        id="3",
        name="Алексей Смирнов",
        nickname="alexsmirnov",
        avatar=None,
        following=[],
        followers=["1"],
        createdAt=datetime(2025, 7, 3, 9, 15, 0)
    )
]
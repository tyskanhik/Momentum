from datetime import datetime
from .models import User

mock_users = [
    User(
        id="1",
        name="Иван Петров",
        avatar="/static/avatar/avtr_1.jpg",
        follower=["2"],
        followers=["2", "3"],
        createdAt=datetime(2025, 7, 1, 10, 0, 0)
    ),
    User(
        id="2",
        name="Мария Иванова",
        avatar="/static/avatar/avtr_2.jpg",
        follower=["1"],
        followers=["1"],
        createdAt=datetime(2025, 7, 2, 12, 30, 0)
    ),
    User(
        id="3",
        name="Алексей Смирнов",
        avatar=None,
        follower=[],
        followers=["1"],
        createdAt=datetime(2025, 7, 3, 9, 15, 0)
    )
]

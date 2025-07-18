from typing import List, Optional
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    nickname: str 
    avatar: Optional[str] = None
    following: List[UUID] = []  
    followers: List[UUID] = []  
    createdAt: datetime

class CardUser(BaseModel):
    id: UUID
    nickname: str
    avatar: Optional[str] = None

class Card(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    link: str
    owner: CardUser
    createdAt: datetime
    likes: List[CardUser] = []
    #comments: Optional[List[str]] = None
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: str
    name: str
    avatar: Optional[str] = None
    follower: List[str] = []  
    followers: List[str] = [] 
    createdAt: datetime

class Card(BaseModel):
    _id: str
    name: str
    description: Optional[str] = None
    link: Optional[str] = None
    owner: str
    createdAt: datetime
    likes: List[str] = []
    #comments: Optional[List[str]] = None
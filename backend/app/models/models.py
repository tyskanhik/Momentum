from typing import List, Optional
from pydantic import BaseModel, Field, validator
from uuid import UUID, uuid4, uuid5, NAMESPACE_OID
from datetime import datetime

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    nickname: str
    avatar: Optional[str] = None
    following: List[UUID] = Field(default_factory=list)
    followers: List[UUID] = Field(default_factory=list)
    createdAt: datetime

    @validator("id", "followers", "following", pre=True, each_item=True)
    def convert_str_to_uuid(cls, v):
        if isinstance(v, str) and v.isdigit():
            return uuid5(NAMESPACE_OID, f"mock-user-{v}")
        return v

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
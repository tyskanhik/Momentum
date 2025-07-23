from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
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

    @field_validator("id", mode="before")
    @classmethod
    def convert_str_to_uuid(cls, v):
        if isinstance(v, str) and v.isdigit():
            return uuid5(NAMESPACE_OID, f"mock-user-{v}")
        return v

    @field_validator("following", "followers", mode="before")
    @classmethod
    def convert_list_str_to_uuid(cls, v):
        if isinstance(v, list):
            return [
                uuid5(NAMESPACE_OID, f"mock-user-{item}") 
                if isinstance(item, str) and item.isdigit() 
                else item 
                for item in v
            ]
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
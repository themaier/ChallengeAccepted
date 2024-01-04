from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class FriendshipTable(SQLModel, table=True):
    __tablename__ = "friendship"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    friend_user_id: str
    status: bool
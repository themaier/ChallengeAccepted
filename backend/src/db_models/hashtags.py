from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class HashtagTable(SQLModel, table=True):
    __tablename__ = "hashtags"

    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    challengeId: int
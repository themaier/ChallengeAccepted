from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class HashtagChallengeTable(SQLModel, table=True):
    __tablename__ = "hashtag_challenge"

    id: Optional[int] = Field(default=None, primary_key=True)
    challenge_id: str = Field(default=None, primary_key=True)
    hashtag_id: int = Field(default=None, primary_key=True)

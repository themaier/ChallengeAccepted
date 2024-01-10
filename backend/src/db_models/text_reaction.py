from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class TextReactionTable(SQLModel, table=True):
    __tablename__ = "text_reactions"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    text: str = Field(default=None, unique=True)
    email: str
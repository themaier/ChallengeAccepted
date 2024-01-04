from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class UserTable(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    email: str
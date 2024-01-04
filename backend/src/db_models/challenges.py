from enum import Enum
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship



class ChallengeStatus(Enum):
    DONE = "done"
    PENDING = "pending"
    DECLINED = "declined"
    ACCEPTED = "accepted"

class ChallengeTable(SQLModel, table=True):
    __tablename__ = "challenges"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    challenge_resources: str
    sender_user_id: str
    receiver_user_id: str
    prove_ressource: str
    status: ChallengeStatus

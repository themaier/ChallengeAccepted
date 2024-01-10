from enum import Enum
from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class ChallengeStatus(Enum):
    DONE = "done"
    PENDING = "pending"
    DECLINED = "declined"
    ACCEPTED = "accepted"

class ChallengeTable(SQLModel, table=True):
    __tablename__ = "challenges"

    id: Optional[int] = Field(default=None, primary_key=True)
    sender_user_id: int
    receiver_user_id: int
    title: str
    description: str
    challenge_resources: str
    prove_resource: str
    done_date: Optional[datetime] = Field()
    status: ChallengeStatus

from typing import List
from fastapi import APIRouter, Depends, Query, HTTPException, Response, status
from src.utils.error import raise_404
from src.db_models.challenges import ChallengeTable
from src.db.session import get_db
from sqlmodel import Session, select

router = APIRouter(tags=["Challenges"])


@router.post("/challenges")
async def add_challenge( 
        challenge: ChallengeTable,
        db: Session = Depends(get_db)):
    db.add(challenge)
    db.commit()
    return 

@router.get("/challenges")
async def get_challenges(
        db: Session = Depends(get_db)
    ) -> List[ChallengeTable]:
    challenges = db.exec(select(ChallengeTable)).all()
    return challenges
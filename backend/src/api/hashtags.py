from typing import List
from fastapi import APIRouter, Depends, Query, HTTPException, Response, status
from src.utils.error import raise_404
from src.db_models.hashtags import HashtagTable
from src.db.session import get_db
from sqlmodel import Session, select

router = APIRouter(tags=["Hashtags"])

@router.post("/hashtags")
async def add_hashtag(
        challengeId: int,
        hashtags: List[str],
        db: Session = Depends(get_db)
    ):
    
    for hashtag in hashtags:
        hashtagTable = HashtagTable()
        hashtagTable.challenge_id = challengeId
        hashtagTable.text = hashtag

        db.add(hashtagTable)

    db.commit()


@router.get("/hashtags")
async def get_hashtags(
        challengeId: int,
        db: Session = Depends(get_db)
    ):
    
    return db.exec(select(HashtagTable)).all()
    

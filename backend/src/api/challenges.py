from typing import List
from fastapi import APIRouter, Depends, Query, HTTPException, Response, status
from src.utils.error import raise_404
from src.db_models.challenges import ChallengeTable, ChallengeStatus
from src.api_models.challenge_accepted import *
from src.db.session import get_db
from sqlmodel import Session, select

router = APIRouter(tags=["Challenges"])


@router.post("/challenges")
async def add_challenge( 
        challenge: ChallengeForm,
        db: Session = Depends(get_db)):

    challenge_entry = ChallengeTable(
        sender_user_id = challenge.friend_id,
        receiver_user_id = challenge.user_id,
        title = challenge.challenge_name,
        description = challenge.description,
        challenge_resources="/",
        prove_resource="/",
        status = ChallengeStatus.PENDING,
    )

    db.add(challenge_entry)
    db.commit()

    hashtags = challenge.hashtags_string.split(',')
    for hashtag in hashtags:
        hashtag_entry = HashtagTable()
        hashtag_entry.challengeId = challenge_entry.id
        hashtag_entry.text = hashtag
        db.add(hashtag_entry)
        
    db.commit()

    return 





@router.get("/challenges")
async def get_challenges(
        db: Session = Depends(get_db)
    ) -> List[ChallengeTable]:
    challenges = db.exec(select(ChallengeTable)).all()
    return challenges


@router.get("/challenges/{userId}/pending")
async def get_pending_challenges(
        userId: str,
        db: Session = Depends(get_db)
    ) -> List[ChallengeTable]:
    challenges = db.exec(select(ChallengeTable).where(ChallengeTable.status == ChallengeStatus.PENDING, ChallengeTable.receiver_user_id == userId))
    return challenges


@router.get("/challenges/{userId}/done")
async def get_pending_challenges(
        userId: str,
        db: Session = Depends(get_db)
    ) -> List[Challenge]:
    challenges = db.exec(select(ChallengeTable).where(ChallengeTable.status == ChallengeStatus.DONE, ChallengeTable.receiver_user_id == userId))
    return challenges


@router.get("/challenges/{userId}/accepted")
async def get_accepted_challenges(
        userId: str,
        db: Session = Depends(get_db)
    ) -> List[Challenge]:
    challenges = db.exec(select(ChallengeTable).where(ChallengeTable.status == ChallengeStatus.ACCEPTED, ChallengeTable.receiver_user_id == userId))
    return challenges


@router.put("/challenges/{id}/accept")
async def accept_challenge(
        challengeId: str,
        db: Session = Depends(get_db)
    ) -> ChallengeTable:
    challenge = db.exec(select(ChallengeTable).where(ChallengeTable.id == challengeId)).first()
    challenge.status = ChallengeStatus.ACCEPTED
    return challenge


@router.put("/challenges/{id}/decline")
async def decline_challenge(
        challengeId: str,
        db: Session = Depends(get_db)
    ) -> ChallengeTable:
    challenge = db.exec(select(ChallengeTable).where(ChallengeTable.id == challengeId)).first()
    challenge.status = ChallengeStatus.DECLINED
    return challenge



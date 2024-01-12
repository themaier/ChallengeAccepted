from datetime import datetime
from typing import List
from sqlalchemy import desc
from sqlmodel import Session, select
from fastapi import APIRouter, Depends, Query, HTTPException, Response, status
from src.utils.error import raise_404
from src.db_models.challenges import ChallengeTable, ChallengeStatus
from src.db_models.hashtag_challenge import HashtagChallengeTable
from src.db_models.text_reaction import TextReactionTable
from src.db_models.users import UserTable
from src.api_models.challenge_accepted import *
from src.db.session import get_db
from src.chatgpt.api_call import check_user_challenge_for_legal

router = APIRouter(tags=["Challenges"])


@router.post("/challenges")
async def add_challenge(
    challenge: ChallengeForm,
    db: Session = Depends(get_db),
):
    if challenge.chatgpt_check:
        answer = check_user_challenge_for_legal(challenge.description)
        if answer == "illegal":
            raise HTTPException(status_code=406, detail="Challenge is illegal.")



    list_hashtags = []
    if(challenge.hashtags_list):
        hashtags = challenge.hashtags_list.split(",")
        
        for hashtag in hashtags:
            existing_hashtag_entry = db.exec(select(HashtagTable).where(HashtagTable.text == hashtag)).first()
            if(existing_hashtag_entry):
                list_hashtags.append(existing_hashtag_entry)
            else:
                hashtag_entry = HashtagTable()
                hashtag_entry.text = hashtag
                list_hashtags.append(hashtag_entry)

    challenge_entry = ChallengeTable(
        sender_user_id = challenge.user_id,
        receiver_user_id = challenge.friend_id,
        title = challenge.challenge_name,
        description = challenge.description,
        reward=challenge.reward,
        challenge_resources="/",
        prove_resource="/",
        status=ChallengeStatus.PENDING,
        hashtags=list_hashtags
    )

    db.add(challenge_entry)
    db.commit()
    
    # if(challenge.hashtags_list):
    #     hashtags = challenge.hashtags_list.split(",")
        
    #     for hashtag in hashtags:
    #         hashtag_entry = HashtagTable()
    #         hashtag_entry.challenge_id = challenge_entry.id
    #         hashtag_entry.text = hashtag
    #         db.add(hashtag_entry)
    #     db.commit()

    #     linktable_entry = HashtagChallengeTable(
    #         challenge_id=challenge_entry.id,
    #         hashtag_id=hashtag_entry.id
    #     )
    #     db.add(linktable_entry)
        # db.commit()
    return 
    


@router.get("/challenges")
async def get_challenges(
        db: Session = Depends(get_db)
     )-> List[Challenge]:

    challenges_entries = db.exec(select(ChallengeTable)).all()
    challenges = map_challenge_list(challenges_entries, db)

    return challenges


def map_challenge_list(
            challenges_entries: List[ChallengeTable],
            db: Session
        ) -> List[Challenge]:
        
        challenges = []

        for challenge in challenges_entries:
            user = db.exec(select(UserTable).where(UserTable.id== challenge.sender_user_id)).first()
            comments = db.exec(select(TextReactionTable).where(TextReactionTable.challenge_id == challenge.id)).all()
            challenge_obj = Challenge(
                id=challenge.id,
                publisher_name=user.username,
                title=challenge.title,
                description = challenge.description,
                prove_resource_path=challenge.prove_resource,
                hashtags=challenge.hashtags,
                comments=comments,
                reward=challenge.reward
            )

            challenges.append(challenge_obj)

        return challenges


@router.get("/challenges/{userId}/pending")
async def get_pending_challenges(
        userId: str,
        db: Session = Depends(get_db)
    ) -> List[Challenge]:

    challenges_entries = db.exec(select(ChallengeTable).where(ChallengeTable.status == ChallengeStatus.PENDING, ChallengeTable.receiver_user_id == userId)).all()
    challenges = map_challenge_list(challenges_entries, db)

    return challenges 


@router.get("/challenges/{userId}/done")
async def get_pending_challenges(
        userId: str,
        db: Session = Depends(get_db)
    ) -> List[Challenge]:

    challenges_entries = db.exec(select(ChallengeTable).where(ChallengeTable.status == ChallengeStatus.DONE, ChallengeTable.receiver_user_id == userId)).all()
    challenges = map_challenge_list(challenges_entries, db)
    return challenges


@router.get("/challenges/{userId}/accepted")
async def get_accepted_challenges(
        userId: int,
        db: Session = Depends(get_db)
    ) -> List[Challenge]:

    challenges_entries = db.exec(select(ChallengeTable).where(ChallengeTable.status == ChallengeStatus.ACCEPTED, ChallengeTable.receiver_user_id == userId)).all()
    challenges = map_challenge_list(challenges_entries, db)
    return challenges


@router.put("/challenges/{id}/comment")
async def accept_challenge(
        challenge_id: int,
        comment: Comment,
        db: Session = Depends(get_db)
    ):
    
    comment_entry = TextReactionTable()
    comment_entry.user_id = comment.user_id
    comment_entry.challenge_id = challenge_id
    comment_entry.text = comment.comment_text
    comment_entry.image_path = comment.comment_image_path

    db.add(comment_entry)
    db.commit()


@router.put("/challenges/{challenge_id}/accept")
async def accept_challenge(
        challenge_id: int,
        db: Session = Depends(get_db)
    ):
    
    challenge = db.exec(select(ChallengeTable).where(ChallengeTable.id == challenge_id)).first()
    challenge.status = ChallengeStatus.ACCEPTED
    
    db.add(challenge)
    db.commit()


@router.put("/challenges/{challenge_id}/done")
async def decline_challenge(
        challengeCompleted: ChallengeCompleted,
        db: Session = Depends(get_db)
    ):
    challenge = db.exec(select(ChallengeTable).where(ChallengeTable.id == challengeCompleted.challenge_id)).first()
    challenge.status = ChallengeStatus.DONE
    challenge.done_date = datetime.now()
    challenge.prove_resource = challengeCompleted.file_path
    
    db.add(challenge)
    db.commit()


@router.put("/challenges/{challenge_id}/decline")
async def decline_challenge(
        challenge_id: int,
        db: Session = Depends(get_db)
    ):
    challenge = db.exec(select(ChallengeTable).where(ChallengeTable.id == challenge_id)).first()
    challenge.status = ChallengeStatus.DECLINED

    db.add(challenge)
    db.commit()


@router.get("/challenges/{hashtag}")
async def decline_challenge(
        hashtag: str,
        db: Session = Depends(get_db)
    ) -> List[Challenge]:

    hashtag_entry = db.exec(select(HashtagTable).where(HashtagTable.text == hashtag)).first()
    challenges = map_challenge_list(hashtag_entry.challenges, db)
    return challenges

    

@router.get("/challenges/latest/{limit}")
async def get_latest_challenges(
        limit: int,
        db: Session = Depends(get_db)
    ) -> List[Challenge]:
    
    latest_entires = db.exec(select(ChallengeTable).order_by(desc(ChallengeTable.done_date)).where(ChallengeTable.status == ChallengeStatus.DONE).limit(limit)).all()
    challenges = map_challenge_list(latest_entires, db)
    return challenges





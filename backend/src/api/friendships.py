from typing import List
from fastapi import APIRouter, Depends, Query, HTTPException, Response, status
from src.utils.error import raise_404
from src.db_models.friendships import FriendshipTable
from src.db.session import get_db
from sqlmodel import Session, select

router = APIRouter(tags=["Friendships"])

@router.get("/friendship")
async def get_all_friendships(
    db: Session = Depends(get_db)
) -> List[FriendshipTable]:
    db_friendships = db.exec(select(FriendshipTable)).all()
    return db_friendships


@router.get("/friendship/{userId}")
async def get_friends_for(
        userId: str,  
        db: Session = Depends(get_db)
) -> List[FriendshipTable]:

    friends = db.exec(select(FriendshipTable).where(FriendshipTable.user_id == userId))
    return friends


@router.post("/friendship")
async def post_new_friendship(
    friendship_request: FriendshipTable,
    db: Session = Depends(get_db)
) -> FriendshipTable:

    friend_request_counterpart = FriendshipTable(
        user_id=friendship_request.friend_user_id,
        friend_user_id=friendship_request.user_id,
        status=True
    )
    
    friend_request_counterpart.user_id, friend_request_counterpart.friend_user_id = friendship_request.friend_user_id, friendship_request.user_id

    db.add(friendship_request)
    db.add(friend_request_counterpart)
    db.commit()
    db.refresh(friendship_request)
    return friendship_request

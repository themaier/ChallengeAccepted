from typing import List
from fastapi import APIRouter, Depends, Query, HTTPException, Response, status
from src.utils.error import raise_404
from src.db_models.friends import FriendsTable
from src.db.session import get_db
from sqlmodel import Session, select

router = APIRouter(tags=["Friends"])

@router.get("/friendship")
async def get_all_friends(
    db: Session = Depends(get_db)
) -> List[FriendsTable]:
    db_friends = db.exec(select(FriendsTable)).all()
    return db_friends


@router.get("/friendship/{userId}")
async def get_friends_for(
        userId: str,  
        db: Session = Depends(get_db)
) -> List[FriendsTable]:

    friends = db.exec(select(FriendsTable).where(FriendsTable.user_id == userId))
    return friends


@router.post("/friendship")
async def post_new_friendship(
    friendship_request: FriendsTable,
    db: Session = Depends(get_db)
) -> FriendsTable:

    friend_request_counterpart = FriendsTable(
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

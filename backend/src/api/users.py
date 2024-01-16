from typing import List
from fastapi import APIRouter, Depends, Query, HTTPException, Response, status
from src.utils.error import raise_404
from src.db_models.users import UserTable
from src.db_models.challenges import ChallengeTable, ChallengeStatus
from src.api_models.users import UserVerify
from src.db.session import get_db
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["Users"])


@router.get("/users")
async def get_all_users(
    db: Session = Depends(get_db),
) -> List[UserTable]:
    db_users = db.exec(select(UserTable)).all()
    return db_users


@router.get("/users/{user_id}")
async def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
) -> UserTable:
    db_user = db.exec(select(UserTable).where(UserTable.id == user_id)).first()
    return db_user


@router.post("/users")
async def post_new_users(
    user: UserTable,
    db: Session = Depends(get_db),
) -> UserTable:
    try:
        db.add(user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Username or email already exists.")
    db.commit()
    db.refresh(user)
    return user


@router.post("/users/verify")
async def verify_login(
    user: UserVerify,
    db: Session = Depends(get_db),
) -> UserTable:
    existingUser = db.exec(
        select(UserTable).where(UserTable.username == user.username)
    ).first()
    if existingUser is None or user.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    if user.challengeId:
        existingChallenge = db.exec(
            select(ChallengeTable).where(ChallengeTable.id == user.challengeId)
        ).first()
        if existingChallenge and existingChallenge.status is ChallengeStatus.ASLINK:
            if existingChallenge.sender_user_id != existingUser.id:
                existingChallenge.status = ChallengeStatus.PENDING
                existingChallenge.receiver_user_id = existingUser.id
                db.add(existingChallenge)
                db.commit()
    return existingUser

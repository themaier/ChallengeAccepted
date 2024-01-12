from pydantic import BaseModel, Field
from typing import Optional, List
from src.db_models.text_reaction import TextReactionTable
from src.db_models.hashtags import HashtagTable
from datetime import datetime



class Challenge(BaseModel):
    id: int
    publisher_name: str
    receiver_name: str
    receiver_id: int
    title: str
    description: str
    prove_resource_path: str
    done_date: Optional[datetime]
    reward: Optional[str]
    comments: Optional[List[TextReactionTable]]
    hashtags: List[HashtagTable]


class LikeChallengeRequest(BaseModel):
    user_id: int
    challenge_id: int


class Comment(BaseModel):
    user_id: int
    comment_text: str
    comment_image_path: str


class ChallengeForm(BaseModel):
    user_id: int
    challenge_name: str
    friend_id: int
    description: str
    hashtags_list: Optional[str]
    reward: Optional[str]
    chatgpt_check: bool

class ChallengeCompleted(BaseModel):
    challenge_id: int
    file_path: str

class Friend(BaseModel):
    user_id: int
    username: str

    


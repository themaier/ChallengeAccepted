from pydantic import BaseModel, Field
from typing import Optional, List
from src.db_models.text_reaction import TextReactionTable
from src.db_models.hashtags import HashtagTable


class Challenge(BaseModel):
    publisher_name: str
    title: str
    description: str
    prove_resource_path: str
    comments: List[TextReactionTable]
    hashtags: List[HashtagTable]


class LikeChallengeRequest(BaseModel):
    user_id: int
    challenge_id: int


class Comment(BaseModel):
    username: str
    comment_text: str
    comment_image_path: str


class ChallengeForm(BaseModel):
    user_id: int
    challenge_name: str
    friend_id: int
    description: str
    hashtags: str
    reward: str
    chatgpt_check: bool

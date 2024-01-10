from pydantic import BaseModel, Field
from typing import Optional, List
from src.db_models.text_reaction import TextReactionTable
from src.db_models.hashtags import HashtagTable

class Post(BaseModel):
    publisher_name: str
    title: str
    description: str
    prove_resource_path: str
    comments: List[TextReactionTable]
    hashtags: List[HashtagTable]
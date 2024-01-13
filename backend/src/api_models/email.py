from pydantic import BaseModel


class Email(BaseModel):
    username: str
    email: str
    frient_username: str

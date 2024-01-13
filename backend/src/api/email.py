from fastapi import APIRouter, BackgroundTasks
from src.api_models.email import Email
from src.email.send_email import send_email_background

router = APIRouter(tags=["Email"])


@router.post("/send-email/backgroundtasks")
def send_email_backgroundtasks(
    background_tasks: BackgroundTasks, email_data: Email
) -> str:
    send_email_background(background_tasks=background_tasks, email_data=email_data)
    return "Success"
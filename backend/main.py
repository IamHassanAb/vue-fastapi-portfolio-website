from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from utils import gmail_send_message

app = FastAPI()

origins = [
    "http://localhost:8080",  # Remove the /* at the end
    "http://127.0.0.1:8080",  # Add alternative localhost address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],  # Be specific instead of *
    allow_headers=["Content-Type"],  # Be specific instead of *
)

class EmailRequest(BaseModel):
    From: str
    Subject: str
    Body: str

@app.post("/send-email/")
async def send_email(email: EmailRequest):
    """Send an email using Gmail API"""
    gmail_send_message(email.From, email.Subject, email.Body)

    return {"message": "Email Sent", "email": email}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
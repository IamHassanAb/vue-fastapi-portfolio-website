import base64
import logging
from email.message import EmailMessage
from pathlib import Path
from typing import Optional, Dict

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define the required OAuth scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def gmail_send_message(From: str, Subject: str, Body: str) -> Optional[Dict]:
    """Create and send an email message using Gmail API"""
    creds = None
    token_path = Path('token.json')
    credentials_path = Path('credentials.json')

    try:
        logger.info("Starting authentication process")
        
        # Try to load existing credentials
        if token_path.exists():
            try:
                logger.debug("Loading credentials from token.json")
                creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
            except ValueError as e:
                logger.warning(f"Token load failed: {str(e)}. Starting fresh auth flow.")
                token_path.unlink()  # Delete invalid token file

        # Handle credential refresh or new auth flow
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    logger.info("Refreshing expired credentials")
                    creds.refresh(Request())
                except Exception as refresh_error:
                    logger.warning(f"Refresh failed: {str(refresh_error)}. Starting fresh auth flow.")
                    creds = None
                    if token_path.exists():
                        token_path.unlink()
            
            if not creds:
                logger.info("Initiating new OAuth flow")
                if not credentials_path.exists():
                    error_msg = "credentials.json file not found"
                    logger.error(error_msg)
                    raise FileNotFoundError(error_msg)
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(credentials_path), SCOPES)
                creds = flow.run_local_server(port=0)
                logger.info("OAuth flow completed successfully")
            
                # Save the new credentials
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())
                logger.debug("Saved new credentials to token.json")

        # Email sending with logging
        logger.info(f"Preparing to send email from {From} with subject: {Subject}")
        service = build("gmail", "v1", credentials=creds)

        message = EmailMessage()
        message.set_content(Body)
        message["To"] = "hassanab220.work@gmail.com"
        message["From"] = From
        message["Subject"] = Subject

        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        create_message = {"raw": encoded_message}

        logger.debug("Sending message via Gmail API")
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        
        logger.info(f"Message sent successfully. Message ID: {send_message['id']}")
        return send_message

    except HttpError as error:
        logger.error(f"Gmail API error occurred: {str(error)}")
        if error.resp.status == 403:
            logger.error("Insufficient permissions. Verify OAuth scopes.")
        return None
    except Exception as error:
        logger.error(f"Unexpected error occurred: {str(error)}", exc_info=True)
        return None
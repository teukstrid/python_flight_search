from twilio.rest import Client
import os

TWILIO_SID = os.environ["TW_SID"]
TWILIO_AUTH_TOKEN = os.environ["TW_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = os.environ["TW_VIRTUAL_NR"]
TWILIO_USER_NUMBER = os.environ["TW_USER_NR"]


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_USER_NUMBER,
        )
        print(message.sid)

import requests
from new import get_new
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def create_message(news_data):
    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)

    for i in news_data:
        body_text = f"Here's an update on {i}: {news_data[i]["title"]} - {news_data[i]["description"]} ({news_data[i]["url"]})"
        
        message = client.messages.create(
            body=body_text,
            from_="+17812197858",
            to="+17812197858"
        )
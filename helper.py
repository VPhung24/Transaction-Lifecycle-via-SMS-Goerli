import os

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
alchemy_key = os.getenv('ALCHEMY_KEY')
from_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
to_phone_number = os.getenv('TWILIO_SEND_UPDATES_TO_PHONE_NUMBER')


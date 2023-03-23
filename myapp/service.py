from twilio.rest import Client
from django.conf import settings
from typing import Tuple


class PhoneNumberService:
    def handle_incoming_sms(self, from_number: str, to_number: str, body: str) -> None:
        print(body)
        pass

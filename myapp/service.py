import requests
from django.http import HttpResponse
from django.conf import settings
from decouple import config
from typing import Tuple


class PhoneNumberService:
    def buy_phone_number(self) -> str:
        account_sid = config("TWILIO_ACCOUNT_SID")
        auth_token = config("TWILIO_AUTH_TOKEN")
        country_code = config("TWILIO_COUNTRY_CODE")
        phone_number_type = config("TWILIO_PHONE_NUMBER_TYPE")
        available_numbers_url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/{phone_number_type}.json'
        response = requests.get(available_numbers_url, auth=(account_sid, auth_token))
        response_json = response.json()

        if 'available_phone_numbers' not in response_json:
            print(f"No phone numbers available")
            raise Exception('No available phone numbers')
        else:
            phone_number = response_json['available_phone_numbers'][0]['phone_number']
            return phone_number
        



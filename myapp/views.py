
import requests
from django.http import HttpResponse
from decouple import config
from twilio.twiml.messaging_response import MessagingResponse

def create_number(request):
    account_sid = config("TWILIO_ACCOUNT_SID")
    auth_token = config("TWILIO_AUTH_TOKEN")
    country_code = config("TWILIO_COUNTRY_CODE")
    phone_number_type = config("TWILIO_PHONE_NUMBER_TYPE")
    print(account_sid)
    available_numbers_url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/{phone_number_type}.json'
    response = requests.get(available_numbers_url, auth=(account_sid, auth_token))
    print(response.status_code)
    print(response.json())
    response_json = response.json()

    if 'available_phone_numbers' not in response_json:
        print(f"No phone numbers available")
        return HttpResponse("No phone numbers available")

    phone_number = response_json['available_phone_numbers'][0]['phone_number']
    incoming_numbers_url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/IncomingPhoneNumbers.json'
    data = {'PhoneNumber': phone_number}
    response = requests.post(incoming_numbers_url, auth=(account_sid, auth_token), data=data)
    print(response.json())
    return HttpResponse(response.json())

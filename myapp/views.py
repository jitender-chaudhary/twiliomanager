
import requests
from django.http import HttpResponse
from decouple import config
from twilio.twiml.messaging_response import MessagingResponse


def sms_webhook(request):
    incoming_number = request.POST.get('From')
    message_body = request.POST.get('Body')
    
    twiml_response = MessagingResponse()
    twiml_response.message("Thank you for your message!")
    
    return HttpResponse(str(twiml_response))
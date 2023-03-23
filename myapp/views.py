
import requests
from rest_framework import views
from rest_framework.response import Response
from .service import PhoneNumberService


class IncomingSMSView(views.APIView):
    def post(self, request) -> Response:
        service = PhoneNumberService()
        from_number = request.data['From']
        to_number = request.data['To']
        body = request.data['Body']
        service.handle_incoming_sms(from_number, to_number, body)
        return Response(status=200)
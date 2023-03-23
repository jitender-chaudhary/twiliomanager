from rest_framework import views
from rest_framework.response import Response
from .serializer import PhoneNumberSerializer
from .service import PhoneNumberService


class PhoneNumberView(views.APIView):
    def post(self, request) -> Response:
        service = PhoneNumberService()
        phone_number = service.buy_phone_number()
        serializer = PhoneNumberSerializer(data={'number': phone_number})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


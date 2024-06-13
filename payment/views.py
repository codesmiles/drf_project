# from django.shortcuts import render

# # Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny
# from .models import Transaction
# from .serializers import TransactionSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.conf import settings
# from rave_python import Rave, RaveExceptions
# import os

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.request import Request


class InitiatePaymentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request:Request):
        url = "https://api.flutterwave.com/v3/payments"
        headers = {
            'Authorization': f'Bearer {"FLWSECK_TEST-2c9735ae68c62f1828a807f922cdc805-X"}',
            'Content-Type': 'application/json'
        }
        
        data = {
            "tx_ref": "MC-1585230ew9v5050e8",
            "amount": request.data.get('amount'),
            "currency": "NGN",
            "redirect_url": "https://your-domain.com/payment-success",
            "payment_type": "card",
            "customer": {
                "email": request.data.get('email'),
                "phonenumber": request.data.get('phone_number'),
                "name": request.data.get('name')
            },
            "customizations": {
                "title": "Test Payment",
                "description": "Payment for test"
            }
        }
        
        response = requests.post(url, json=data, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(response.json(), status=response.status_code)
        

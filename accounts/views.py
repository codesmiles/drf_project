from django.shortcuts import render
from .serializers import signUpSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
# Create your views here.

class SIgnUpView(generics.GenericAPIView):
    serializer_class = signUpSerializer
    
    def post(self, request:Request):
        data = request.data
        
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                "successful": True,
                "response": "Success",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        response = {
            "successful": False,
            "response": "Error",
            "data": serializer.errors
            }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
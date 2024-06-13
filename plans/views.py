from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Plan
from .serializers import PlanSerializer
# Create your views here.

class PlanViewset(viewsets.ModelViewSet): #model viewset helps you to construct crud operations without the long stories
    queryset= Plan.objects.all()
    serializer_class = PlanSerializer
    
    
    
    
    
# class PlanViewset(viewsets.ViewSet):
#     def list(self, request:Request):
#         querySet = Plan.objects.all()
#         serializer = PlanSerializer(querySet, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def retrieve(self, request:Request, pk=None):
#         plan = get_object_or_404(Plan, pk=pk)
        
#         serializer = PlanSerializer(instance=plan)
        
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    

from rest_framework import serializers
from .models import Plan

class PlanSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    detail = serializers.CharField()
    status = serializers.BooleanField(default=False)

    
    class Meta:
        model = Plan
        fields = ['id', 'name', 'detail', "status", 'created']
        
    
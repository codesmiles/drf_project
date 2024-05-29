from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    
    class Meta:
        model = Comment
        fields = ['id', 'title', 'description', "status", 'created']
        
    
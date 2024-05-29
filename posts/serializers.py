from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created'] #way better inheriting from ModelSerializer
        
    
    
    # WHEN INHERITING FROM PLAIN SERIALIZER
    # id= serializers.IntegerField(read_only=True) 
    # title = serializers.CharField(max_length=50)
    # content = serializers.CharField()
    # created = serializers.DateTimeField(read_only=True)
# serializer.data
# serializer.error
    
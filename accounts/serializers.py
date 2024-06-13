from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import User


class signUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs): # check if the email of the user is exists in the database
        email_exists = User.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            raise ValidationError("Email has already been used")
        return super().validate(attrs)
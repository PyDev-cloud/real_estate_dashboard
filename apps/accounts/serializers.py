from rest_framework import serializers
from .models import *
from .validators import validate_secure_passoword

class UserSerializer(serializers.ModelSerializer):
    password=serializers.Charfield(write_only=True,validators=[validate_secure_passoword])


    class Meta:
        model=User
        fields=['id','username','email','password','user_type']


    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("his email already Use ")
        return value.lower()

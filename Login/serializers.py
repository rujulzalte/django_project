from rest_framework import serializers
from . models import UserLogin

class UserLoginSerial(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = ['id','first_name', 'last_name', 'username', 'password', 'Phone_no', 'state']
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterAdminSerializer(serializers.ModelSerializer):
    phone_num=serializers.CharField()
    age = serializers.IntegerField()
    position = serializers.CharField()
    gender = serializers.CharField()
    signature = serializers.ImageField(required=True)
    profile_picture = serializers.ImageField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','password','phone_num','age','gender','signature','position','profile_picture']
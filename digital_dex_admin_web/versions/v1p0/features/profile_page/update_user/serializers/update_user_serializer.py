from rest_framework import serializers
from .......models.admin_model import Admin
from django.contrib.auth.models import User
from datetime import datetime


class UpdateUserSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['phone_num', 'birthday']


class UpdateUserSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'email']

        
    
def validate_birthday(self, value):
    date_obj = datetime.strptime(value, '%m-%d-%Y').date()
    date_str = date_obj.strftime('%Y-%m-%d')
    formatted_date = datetime.strptime(date_str, '%m-%d-%Y').date()
    return formatted_date
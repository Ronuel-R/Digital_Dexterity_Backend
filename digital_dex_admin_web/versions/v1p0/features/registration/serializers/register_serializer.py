from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime

class RegisterAdminSerializer(serializers.ModelSerializer):
    phone_num=serializers.CharField()
    gender = serializers.CharField()
    position_level = serializers.CharField()
    birthday=serializers.DateField(format="%m/%d/%Y", input_formats=['%m/%d/%Y'])
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','password','phone_num','birthday','gender','position_level']

def validate_birthday(self, value):
    # Convert the date string to a date object
    date_obj = datetime.strptime(value, '%m/%d/%Y').date()
    # Format the date object as a string in the desired format
    date_str = date_obj.strftime('%Y/%m/%d')
    # Parse the formatted string as a date object
    formatted_date = datetime.strptime(date_str, '%m/%d/%Y').date()
    return 
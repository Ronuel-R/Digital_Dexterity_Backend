from rest_framework import serializers
from django.contrib.auth.models import User
from .......models.admin_model import Admin

class ProfilePageSerializerAdmin(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ['phone_num', 'birthday', 'position_level']


class ProfilePageSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',  'email']


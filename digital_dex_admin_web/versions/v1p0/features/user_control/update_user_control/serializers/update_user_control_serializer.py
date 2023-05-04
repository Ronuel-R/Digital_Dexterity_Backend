from rest_framework import serializers
from .......models.admin_model import Admin


class UserControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['id','position_level']



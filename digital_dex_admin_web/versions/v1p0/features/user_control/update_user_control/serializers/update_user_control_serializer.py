from rest_framework import serializers
from .......models.admin_model import Admin


class UserControlSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Admin
        fields = ['id', 'full_name','first_name','last_name','position_level']

    def get_full_name(self, obj):
        user = obj.user
        return f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else None


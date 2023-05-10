from rest_framework import serializers
from .......models.admin_model import Admin

class UserControlSerializerAdmin(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)
    email = serializers.CharField(source='user.email', required=False)
    full_name = serializers.SerializerMethodField()
    position_level_display = serializers.CharField(source='get_position_level_display')
    user_id = serializers.SerializerMethodField(source='user.id', required=False)

    class Meta:
        model = Admin
        fields = ['id', 'first_name', 'last_name', 'full_name','email', 'position_level', 'position_level_display','user_id']

    def get_full_name(self, obj):
        user = obj.user
        return f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else None

    def get_user_id(self, obj):
        return obj.user.id if obj.user else None

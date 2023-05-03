from rest_framework import serializers
from .......models.admin_model import Admin

class ProfilePageSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)
    email = serializers.EmailField(source='user.email', required=False)
    phone_num = serializers.CharField(required=False)
    birthday = serializers.DateField(required=False)
    position_level = serializers.CharField(source='get_position_level_display')
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Admin
        fields = ['first_name', 'last_name', 'full_name', 'email', 'phone_num', 'birthday', 'position_level']

    def get_full_name(self, obj):
        user = obj.user
        return f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else None
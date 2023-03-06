from rest_framework import serializers
from ......models.admin_model import Admin

class ProfilePageSerializer(serializers.Serializer):
    user = serializers.CharField(source='user.username')
    profile_picture = serializers.ImageField(required=False)
    full_name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)
    phone_num = serializers.CharField(required=False)
    position = serializers.CharField(required=False)
    signature = serializers.ImageField(required=False)

    class Meta:
        model = Admin
        fields = ['user', 'profile_picture', 'full_name', 'age', 'gender', 'phone_num', 'position', 'signature']


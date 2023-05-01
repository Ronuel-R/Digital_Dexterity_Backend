from rest_framework import serializers
from ......models.admin_model import Admin

class ProfilePageSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    profile_picture = serializers.ImageField(required=False)
    full_name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)
    phone_num = serializers.CharField(required=False)
    position = serializers.CharField(required=False)

    class Meta:
        model = Admin
        fields = ['user', 'profile_picture', 'full_name', 'age', 'gender', 'phone_num', 'position']

 
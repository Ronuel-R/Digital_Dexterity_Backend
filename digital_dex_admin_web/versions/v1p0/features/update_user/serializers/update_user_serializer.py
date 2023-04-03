from rest_framework import serializers
from ......models.admin_model import Admin

class UpdateUserSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',required=False)
    email = serializers.EmailField(source='user.email',required=False)
    first_name = serializers.CharField(source='user.first_name',required=False)
    last_name = serializers.CharField(source='user.last_name',required=False)
    profile_picture = serializers.ImageField(required=False)
    full_name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    gender = serializers.CharField(required=False)
    phone_num = serializers.CharField(required=False)
    position = serializers.CharField(required=False)
    signature = serializers.ImageField(required=False)

    class Meta:
        model = Admin
        fields = ['user', 'email', 'first_name', 'last_name', 'full_name', 'profile_picture', 'age', 'gender', 'phone_num', 'position', 'signature']

    def update(self, instance, validated_data):
        user_data = validated_data.get('user', {})
        username = user_data.get('username', instance.user.username)
        email = user_data.get('email', instance.user.email)
        first_name = user_data.get('first_name', instance.user.first_name)
        last_name = user_data.get('last_name', instance.user.last_name)

        instance.user.username = username
        instance.user.email = email
        instance.user.first_name = first_name
        instance.user.last_name = last_name

        instance.profile_picture = validated_data.get('profile_picture', instance.profile_picture)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone_num = validated_data.get('phone_num', instance.phone_num)
        instance.position = validated_data.get('position', instance.position)
        instance.signature = validated_data.get('signature', instance.signature)

        password = validated_data.get('password', None)
        if password is not None:
            instance.user.set_password(password)

        instance.user.save()
        instance.save()
        return instance
    
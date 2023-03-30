from rest_framework.views import APIView
from ..serializers.login_serializer import LoginAdminSerializer
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework import status
from django.contrib.auth.models import User
from constants.http_messages import *


class LoginAdminView(APIView):
    
    serializer_class = LoginAdminSerializer
    
    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            message = 'Invalid Value Error'
            status = bad_request
            return Response({"status": status , "message": message ,  "data": data , "errors": serializer.errors})

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        
        errors = self.validate_email_and_password(email, password)
        
        if errors:
            message = 'Invalid Value Error'
            status = bad_request
            return Response({"status": status , "message": message ,  "data": data , "errors": serializer.errors})
        

        user = self.authenticate_user(email, password)
        if user:
            login(request, user)
            status = ok
            message = ' Logged in Successfully'
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        else:
            message = 'User not authenticated'
            status = unauthorized
            errors = serializer.errors
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})



    def validate_email_and_password(self, email, password):
        errors = {}
        if not email:
            errors['email'] = ['Email is required.']
        if not password:
            errors['password'] = ['Password is required.']
        if email and not User.objects.filter(email=email).exists():
            errors['email'] = ['Invalid email.']
        if password and email and not self.authenticate_user(email, password):
            errors['password'] = ['Invalid password.']

        return errors


    def authenticate_user(self, email, password):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if not user.check_password(password):
            return None

        return user
    
    

    
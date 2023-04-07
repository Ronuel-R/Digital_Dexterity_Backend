from rest_framework.views import APIView
from ..serializers.login_serializer import LoginAdminSerializer
from rest_framework.response import Response
from django.contrib.auth import login

############ CONSTANTS ##################
from constants.login_helper import LoginHelper
from constants.http_messages import *
from constants.login_helper import LoginHelper
from django.middleware.csrf import get_token


class LoginAdminView(APIView):
    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None
        if request.user.is_authenticated:
            message = 'You are already logged in'
            status = ok
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        
        serializer = LoginAdminSerializer(data=request.data)

        if not serializer.is_valid():
            message = 'Invalid Value Error'
            status = bad_request
            return Response({"status": status , "message": message ,  "data": data , "errors": serializer.errors})

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        
        errors = LoginHelper.validate_email_and_password(self,email, password)
        
        if len(errors) != 0:
            message = 'Invalid Value Error'
            status = bad_request
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        user = LoginHelper.authenticate_user(self, email, password)

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
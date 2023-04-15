from rest_framework.views import APIView
from ..serializers.login_serializer import LoginAdminSerializer
from rest_framework.response import Response


############ CONSTANTS ##################
from constants.login_helper import LoginHelper
from constants.http_messages import *

import jwt
import datetime

class LoginAdminView(APIView):
    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        token = request.COOKIES.get('jwt')

        if token:
            errors = 'Used Token'
            status = bad_request
            message = 'You are already logged in'
            return Response({"status": status, "message": message, "data": data, "errors": errors})
        
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
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }
            token = jwt.encode(payload, 'secret', algorithm='HS256')

            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {
            'status' : ok,
            'message': 'Login Successfully',
            "data": data,
            "errors": errors
        }
            status = ok
            message = 'Logged in Successfully'
            return response
        
        else:
            
            message = 'User not authenticated'
            status = unauthorized
            errors = serializer.errors
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
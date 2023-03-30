from rest_framework.views import APIView
from ..serializers.login_serializer import LoginAdminSerializer
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework import status
from django.contrib.auth.models import User
from constants.http_messages import *

class LogoutAdminView(APIView):
    def get(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        if not request.user.is_authenticated:
            message = 'You are not logged in'
            status = unauthorized
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})

        try:

            logout(request)

            status = ok
            message = 'Logged out Successfully'

            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        except Exception as e:
            message = 'Internal 500 error'
            status = internal_server_error
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
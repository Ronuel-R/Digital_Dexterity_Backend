from rest_framework.views import APIView
from ..serializers.register_serializer import RegisterAdminSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from ......models.admin_model import Admin
# from constants.register_helper import RegisterHelper
# from constants.permission_checker_helper import PermissionChecker

# ################### Consants #####################
# from constants.auth_user import AuthUser
# from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class RegisterAdminView(APIView):
    def post(self,request):
        errors = {}
        data = {}
        status = None
        message = None

        # token = AuthUser.get_token(request)

        # if type(token) == dict:
        #     return Response(token)

        # payload = AuthUser.get_user(token)

        # if 'errors' in payload:
        #     return Response(payload)

        # errors = RegisterHelper.validate_data(request)

        # # errors = PermissionChecker.validate_permission_add_user(self,payload)

        # if len(errors) != 0:
        #     status = bad_request
        #     message = 'Invalid Value'
        #     return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        serializer = RegisterAdminSerializer(data=request.data)
        
        if serializer.is_valid():
            Admin.objects.create(
                user = User.objects.create(
                    first_name= request.data['first_name'],
                    last_name= request.data['last_name'],
                    username = request.data['first_name'],
                    email= request.data['email'],
                    password= make_password(request.data['password'])
                    ),
                birthday = serializer.validated_data['birthday'],
                phone_num= request.data['phone_num'],
                gender = request.data['gender'],
                position_level = request.data['position_level'],
                full_name = request.data['first_name'] + ' ' + request.data['last_name'],
            )
            print(serializer.data)
            status = created
            message = 'Account Successfully Created'
            data = serializer.data
            errors = serializer.errors

        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors
        return Response({"status": status , "message": message ,  "data": data , "errors": errors})
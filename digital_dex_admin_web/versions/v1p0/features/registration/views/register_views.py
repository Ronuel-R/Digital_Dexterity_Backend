from rest_framework.views import APIView
from ..serializers.register_serializer import RegisterAdminSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from ......models.admin_model import Admin
from constants.http_messages import *
from constants.register_helper import RegisterHelper

class RegisterAdminView(APIView):
    errors = {}
    def post(self,request):
        errors = {}
        data = {}
        status = None
        message = None

        errors = RegisterHelper.validate_data(request)

        if len(errors) != 0:
            status = ok
            message = 'Invalid Value'
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        serializer = RegisterAdminSerializer(data=request.data)
        
        errors = self.errors

        if len(errors) != 0:
            status = ok
            message = 'Invalid Value'
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
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
                full_name = request.data['first_name'] + ' ' + request.data['last_name'],
            )
            print(serializer.data)
            status = created
            message = 'Account Successfully Created'
            data = serializer.data
            errors = serializer.errors

        else:

            status = ok
            message = 'Invalid Value'
            errors = serializer.errors
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        return Response({"status": status , "message": message ,  "data": data , "errors": errors})
    
    
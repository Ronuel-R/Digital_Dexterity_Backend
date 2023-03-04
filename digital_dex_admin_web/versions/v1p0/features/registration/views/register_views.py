from rest_framework.views import APIView
from ..serializers.register_serializer import RegisterAdminSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from ......models.admin_model import Admin
from constants.http_messages import *

class RegisterAdminView(APIView):
    errors = {}
    def post(self,request):
        errors = {}
        data = {}
        status = None
        message = None
        
        serializer = RegisterAdminSerializer(data=request.data)
        
        self.validate_data(request)
        
        errors = self.errors

        if len(errors) != 0:
            status = ok
            message = 'Invalid Value'
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        self.validate_image(request)

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
                profile_picture = request.data['profile_picture'],
                phone_num= request.data['phone_num'],
                age = request.data ['age'],
                gender = request.data['gender'],
                position = request.data['position'],
                signature = request.data['signature'],
                full_name = request.data['first_name'] + ' ' + request.data['last_name'],
            )
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
    
    def validate_data(self,request):
        errors = {}

        if request.data['first_name'] and User.objects.filter(username=request.data["first_name"]).count() != 0:
            errors['first_name'] = 'First name is already used'

        if request.data['email'] and User.objects.filter(email=request.data["email"]).count() != 0:
            errors['email'] = 'Email has already been used'

        if request.data['password'] != request.data['confirm_password']:
            errors['password'] = 'Password does not match'

        if len(request.data['phone_num']) != 11:
            errors['phone_number'] = 'Please Enter a valid phone number'

        if request.data['phone_num'][:2] != '09':
            errors['phone_number'] = 'Please Enter Philippine-based mobile number'

        self.errors = errors

        return self.errors
    
    def validate_image(self,request):
        errors = {}
        
        if 'signature' in request.data:
            if request.data['signature'] != '':
                signature_size = request.data['signature'].size
                signature_ext = request.FILES["signature"]
                
                if float(signature_size) > 5000000:
                    errors['signature_size'] = "You cannot upload file more than 5Mb"

                if signature_ext.content_type != 'image/png' and signature_ext.content_type != 'image/jpeg':
                    errors['signature_ext'] = "Only use .PNG files or .JPEG files"

        if 'profile_picture' in request.data:
            if request.data['profile_picture'] != '':
                profile_picture_size = request.data['profile_picture'].size
                profile_picture_ext = request.FILES["profile_picture"]

                if float(profile_picture_size) > 5000000:
                    errors['profile_size'] = "You cannot upload file more than 5Mb"
                    
                if profile_picture_ext.content_type != 'image/png' and profile_picture_ext.content_type != 'image/jpeg':
                    errors['profile_ext'] = "Only use .PNG files or .JPEG files"
            
        self.errors = errors

        return self.errors
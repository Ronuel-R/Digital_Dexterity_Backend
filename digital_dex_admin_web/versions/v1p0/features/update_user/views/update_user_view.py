from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from rest_framework import status
from digital_dex_admin_web.models.admin_model import Admin
from ..serializers.update_user_serializer import UpdateUserSerializer
from constants.update_profile_helper import UpdateHelper

class UpdateUserView(APIView):
    def put(self, request):
        data = {}
        errors = {}
        status_code = None
        message = None
        
        if not request.user.is_authenticated:
            raise Exception('You are not logged in')

        admin = Admin.objects.filter(user=request.user).first()

        serializer = UpdateUserSerializer(admin, data=request.data, partial=True)
        
        if serializer.is_valid():
            update_helper = UpdateHelper()
            validation_errors = update_helper.validate_fields(request) 
            
            if validation_errors:
                errors.update(validation_errors)
                status_code = status.HTTP_400_BAD_REQUEST
            else:
                serializer.save()
                data = serializer.data
                status_code = status.HTTP_200_OK
                message = 'User updated successfully'
        else:
            errors = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST

        if errors:
            message = 'There are validation errors'

        return Response({"status": status_code, "message": message, "data": data, "errors": errors})
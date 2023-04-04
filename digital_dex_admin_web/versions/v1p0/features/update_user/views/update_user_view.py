from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from digital_dex_admin_web.models.admin_model import Admin
from ..serializers.update_user_serializer import UpdateUserSerializer
from constants.update_profile_helper import UpdateHelper

class UpdateUserView(APIView):
    def put(self, request):
        data = {}
        errors = {}
        status = None
        message = None
        
        if not request.user.is_authenticated:
            message = 'You are not logged in'
            status = unauthorized
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        
        admin = Admin.objects.filter(user=request.user).first()

        serializer = UpdateUserSerializer(admin, data=request.data, partial=True)
        
        if serializer.is_valid():

            validation_errors = UpdateHelper.validate_fields(request) 
            
            if validation_errors:
                errors.update(validation_errors)
                status = bad_request
            else:
                serializer.save()
                data = serializer.data
                status = ok
                message = 'User updated successfully'
        else:
            errors = serializer.errors
            status = bad_request

        if errors:
            message = 'There are validation errors'

        return Response({"status": status, "message": message, "data": data, "errors": errors})
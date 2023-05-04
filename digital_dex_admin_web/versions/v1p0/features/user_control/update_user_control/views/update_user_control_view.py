from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from .......models.admin_model import Admin
from constants.auth_user import AuthUser
from ..serializers.update_user_control_serializer import UserControlSerializer
from constants.permission_checker_helper import PermissionChecker

class UpdateUserControlView(APIView):
    def put(self, request):
        errors = {}
        data = []
        status = None
        message = None


        token = AuthUser.get_token(request)

        if isinstance(token, dict):
            return Response(token)

        payload = AuthUser.get_user(token)

        if 'errors' in payload:
            return Response(payload)
        
        errors = PermissionChecker.validate_permission_control(self, payload)

        if len(errors) != 0:
            status = bad_request
            message = 'Invalid Input'
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        try:
            admin_id = request.query_params.get('id')
            admin = Admin.objects.get(id=admin_id)

            user_first_name = admin.user.first_name
            serializer = UserControlSerializer(instance=admin, data=request.data , partial=True)
            if serializer.is_valid():
                serializer.save()
                serialized_data = serializer.data
                user_first_name = admin.user.first_name
                user_last_name = admin.user.last_name
                user_full_name = f"{user_first_name} {user_last_name}"
                data = {
                'id': serialized_data.get('id', None),
                'full_name': user_full_name,
                'position_level': serialized_data.get('position_level', None),
            }
                message = 'User control updated successfully'
                status = ok
            else:
                errors = serializer.errors

        except Admin.DoesNotExist:
            errors = {'admin': 'Admin does not exist'}
            message = 'Admin not found'
            status = not_found


        return Response({"status": status, "message": message, "data": data, "errors": errors})
from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from .......models.admin_model import Admin
from ..serializers.display_user_control_serializer import UserControlSerializerAdmin
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker

class UserControlView(APIView):
    def get(self, request):
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
            admins = Admin.objects.all()
            admin_serializer = UserControlSerializerAdmin(admins, many=True)
            serialized_data = admin_serializer.data
            data = []
            for serialized_obj in serialized_data:
                data.append({
                    'id': serialized_obj.get('id', None),
                    'first_name': serialized_obj.get('first_name', None),
                    'last_name': serialized_obj.get('last_name', None),
                    'full_name': serialized_obj.get('full_name', None),
                    'position_level': serialized_obj.get('position_level', None),
                })
            status = 'ok'
            message = 'Successfully Retrieved User Conrtrol Information'

        except Exception as e:
            errors = {'error': str(e)}
            status = 'bad_request'
            message = 'Bad Request'

        return Response({"status": status, "message": message, "data": data, "errors": errors})
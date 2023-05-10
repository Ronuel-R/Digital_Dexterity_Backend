from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from .......models.admin_model import Admin
from ..serializers.display_user_control_serializer import UserControlSerializerAdmin
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker

class UserControlView(APIView):
    def get(self, request, *args, **kwargs):
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
            message = 'You are not permitted to access User Control'
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        try:
            id = request.query_params["id"]
            admins = Admin.objects.filter(id =id).first()
            admin_serializer = UserControlSerializerAdmin(admins)
            serialized_data = admin_serializer.data
            data = admin_serializer.data
            status = ok
            message = 'Successfully Retrieved User Control Information'

        except:
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
                    'email': serialized_obj.get('email', None),
                    'position_level': serialized_obj.get('position_level', None),
                    'position_level_display': serialized_obj.get('position_level_display', None),
                    'user_id': serialized_obj.get('user_id', None),
                })
            status = ok
            message = 'Successfully Retrieved User Control Information'

        return Response({"status": status, "message": message, "data": data, "errors": errors})
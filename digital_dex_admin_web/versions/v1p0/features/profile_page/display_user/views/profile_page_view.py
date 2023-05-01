from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from .......models.admin_model import Admin
from django.contrib.auth.models import User
from rest_framework import status
from ..serializers.profile_page_serializer import ProfilePageSerializerAdmin, ProfilePageSerializerUser
from constants.auth_user import AuthUser

class ProfilePageView(APIView):
    def get(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        token = AuthUser.get_token(request)

        if type(token) == dict:
            return Response(token)

        payload = AuthUser.get_user(token)

        if 'errors' in payload:
            return Response(payload)

        try:
            user = User.objects.filter(id=payload['id']).first()
            admin = Admin.objects.filter(id=payload['admin_id']).first()

            if admin:
                admin_serializer = ProfilePageSerializerAdmin(admin)
                user_serializer = ProfilePageSerializerUser(user)
                data = {
                    'first_name': user_serializer.data.get('first_name', None),
                    'last_name':  user_serializer.data.get('last_name', None),
                    'email': user_serializer.data.get('email', None),
                    'birthday': admin_serializer.data.get('birthday', None),
                    'phone_num': admin_serializer.data.get('phone_num', ''),
                    'position_level': admin_serializer.data.get('position_level', None),
                }
                status = 'ok'
                message = 'Successfully Retrieved Profile Information'
            else:
                errors = {'error': 'Admin not found'}
                status = 'not_found'
                message = 'Admin not found'

        except Exception as e:
            errors = {'error': str(e)}
            status = 'bad_request'
            message = 'Bad Request'

        return Response({"status": status, "message": message, "data": data, "errors": errors})

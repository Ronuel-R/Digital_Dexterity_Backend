from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from .......models.admin_model import Admin
from django.contrib.auth.models import User
from rest_framework import status
from ..serializers.profile_page_serializer import ProfilePageSerializer
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
            user = User.objects.get(id=payload['id'])
            admin = user.admin

            serializer = ProfilePageSerializer(admin)
            serialized_data = serializer.data
            data = {
                'first_name': serialized_data.get('first_name', None),
                'last_name': serialized_data.get('last_name', None),
                'full_name': serialized_data.get('full_name', None),
                'email': serialized_data.get('email', None),
                'birthday': serialized_data.get('birthday', None),
                'phone_num': serialized_data.get('phone_num', ''),
                'position_level': serialized_data.get('position_level', None),
            }
            status = 'ok'
            message = 'Successfully Retrieved Profile Information'

        except Exception as e:
            errors = {'error': str(e)}
            status = 'bad_request'
            message = 'Bad Request'

        if not admin:
            errors = {'error': 'Admin not found'}
            status = 'not_found'
            message = 'Admin not found'

        return Response({"status": status, "message": message, "data": data, "errors": errors})


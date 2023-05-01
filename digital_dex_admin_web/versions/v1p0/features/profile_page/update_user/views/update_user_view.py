from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from .......models.admin_model import Admin
from django.contrib.auth.models import User
from ..serializers.update_user_serializer import UpdateUserSerializerAdmin, UpdateUserSerializerUser
from constants.auth_user import AuthUser

class UpdateUserView(APIView):
    def put(self, request):
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
        
        admin = Admin.objects.filter(id=payload['admin_id']).first()
        user = User.objects.filter(id=payload['id']).first()

        serializerAdmin = UpdateUserSerializerAdmin(admin, data=request.data, partial=True)
        serializerUser = UpdateUserSerializerUser(user, data=request.data, partial=True)

        if serializerAdmin.is_valid():
            if serializerUser.is_valid():
                serializerUser.save()
                serializerAdmin.save()
            data = serializerUser.validated_data
            data.update(serializerAdmin.validated_data)
            data = data
            status = ok
            message = 'User Profile updated successfully'
        else:
            errors = serializerAdmin.errors or serializerUser.errors
            status = bad_request

        if errors:
            message = 'There are validation errors'

        return Response({"status": status, "message": message, "data": data, "errors": errors})
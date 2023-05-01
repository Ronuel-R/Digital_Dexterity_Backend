from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from ......models.admin_model import Admin
from rest_framework import status
from ..serializers.profile_page_serializer import ProfilePageSerializer


class ProfilePageView(APIView):
    def get(self, request):
        errors = {}
        data = {}
        status_code = None
        message = None

        try:
            if not request.user.is_authenticated:
                message = 'You are not logged in'
                status = unauthorized
                return Response({"status": status, "message": message, "data": data, "errors": errors})

            admin = Admin.objects.filter(user=request.user).first()

            if admin:
                serializer = ProfilePageSerializer(admin)
                serialized_data = serializer.data

                data = {
                    'user': serialized_data.get('user', None),
                    'profile_picture': serialized_data.get('profile_picture', None),
                    'full_name': serialized_data.get('full_name', ''),
                    'age': serialized_data.get('age', None),
                    'gender': serialized_data.get('gender', None),
                    'phone_num': serialized_data.get('phone_num', ''),
                    'position': serialized_data.get('position', ''),
                }
            status = ok
            message = 'Success'

        except Exception as e:
            errors = str(e)
            status = bad_request
        
        return Response({"status": status, "message": message, "data": data, "errors": errors})

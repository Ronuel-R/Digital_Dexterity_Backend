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
                raise Exception('You are not logged in')

            admin = Admin.objects.filter(user=request.user).first()

            if admin:
                serializer = ProfilePageSerializer(admin)
            data = serializer.data
                
            status_code = status.HTTP_200_OK
            message = 'Success'

        except Exception as e:
            errors['message'] = str(e)
            status_code = status.HTTP_400_BAD_REQUEST

        return Response({"status": status_code, "message": message, "data": data, "errors": errors})
    


 
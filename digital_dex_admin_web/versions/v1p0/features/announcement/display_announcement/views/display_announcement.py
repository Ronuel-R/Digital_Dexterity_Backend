from rest_framework.views import APIView
from rest_framework.response import Response
from .......models.announcement_model import Announcement
from ....announcement.display_announcement.serializers.display_announcement import DisplayAnnouncementSerializer
# from channels.layers import get_channel_layer
################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class DisplayAnnouncement(APIView):
    def get(self,request):
        errors = {}
        data = {}
        status = None
        message = None

        # token = AuthUser.get_token(request)

        # if type(token) == dict:
        #     return Response(token)

        # payload = AuthUser.get_user(token)

        # if 'errors' in payload:
        #     return Response(payload)
        
        announcement = list(Announcement.objects.all().values('message'))
        announcement_serializer = DisplayAnnouncementSerializer(data = announcement,many=True)

        if announcement_serializer.is_valid():

            data['announcement'] = announcement_serializer.data
            status = ok
            message= 'Success'
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        else:
            status = bad_request
            message= 'Invalid Data'
            errors = announcement_serializer.errors
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
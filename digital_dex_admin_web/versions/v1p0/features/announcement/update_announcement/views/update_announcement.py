from rest_framework.views import APIView
from rest_framework.response import Response
from .......models.announcement_model import Announcement
from ..serializers.update_announcement import UpdateAnnouncementSerializer
# from channels.layers import get_channel_layer
################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class UpdateAnnouncement(APIView):
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

        id = request.data['id']
        if id:
            try:
                assessment = Announcement.objects.get(pk=id)
                serializer = UpdateAnnouncementSerializer(instance=assessment, data=request.data['message'],partial=True)
                if serializer.is_valid():
                    serializer.save()
                else:
                    errors.update(serializer.errors)
            except Announcement.DoesNotExist:
                pass

            status = ok
            message = 'Successfully updated Announcement'
            data = serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'

        return Response({"status": status, "message": message, "data": data, "errors": errors})
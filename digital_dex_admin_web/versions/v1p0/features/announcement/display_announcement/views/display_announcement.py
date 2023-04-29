from rest_framework.views import APIView
from rest_framework.response import Response
from .......models.announcement_model import Announcement
from ....announcement.display_announcement.serializers.display_announcement import DisplayAnnouncementSerializer
from constants.http_messages import *
from channels.layers import get_channel_layer

class DisplayAnnouncement(APIView):
    def get(self,request):
        errors = {}
        data = {}
        status = None
        message = None

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
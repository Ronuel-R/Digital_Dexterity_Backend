from rest_framework.views import APIView
from rest_framework.response import Response
from .......models.announcement_model import Announcement
from ..serializers.update_announcement import UpdateAnnouncementSerializer
from constants.http_messages import *
from channels.layers import get_channel_layer

class UpdateAnnouncement(APIView):
    def get(self,request):
        errors = {}
        data = {}
        status = None
        message = None

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
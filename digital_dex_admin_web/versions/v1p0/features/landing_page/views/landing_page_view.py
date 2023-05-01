from rest_framework.views import APIView
from rest_framework.response import Response
from ..websocket.landing_page_socket import LandingPageConsumer
from ......models.tax_form_model import TaxForm
from ......models.tax_initial_assessment_model import InitialAssessment
from ......models.announcement_model import Announcement
from ...announcement.display_announcement.serializers.display_announcement import DisplayAnnouncementSerializer
from django.db.models import Count, DateTimeField
from django.db.models.functions import TruncWeek
from channels.layers import get_channel_layer
################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class LandingPageView(APIView):
    def get(self,request):
        errors = {}
        data = {}
        status = None
        message = None
        # admin_consumer = LandingPageConsumer()
        # admin_consumer.channel_layer = get_channel_layer
        # admin_consumer.room_group_name = 'Admin'

        # token = AuthUser.get_token(request)

        # if type(token) == dict:
        #     return Response(token)

        # payload = AuthUser.get_user(token)

        # if 'errors' in payload:
        #     return Response(payload)

        total_tax_dec = TaxForm.objects.values(week=TruncWeek('date_modified')).annotate(total_updates=Count('date_modified')
        ).order_by('-week').first()
        announcement = list(Announcement.objects.all().values('message'))
        announcement_serializer = DisplayAnnouncementSerializer(data = announcement,many=True)

        if announcement_serializer.is_valid():

            residential = InitialAssessment.objects.filter(classification = 'R').count()
            agricultural = InitialAssessment.objects.filter(classification = 'A').count()
            commercial = InitialAssessment.objects.filter(classification = 'C').count()
            industrial = InitialAssessment.objects.filter(classification = 'I').count()
            special = InitialAssessment.objects.filter(classification = 'S').count()
            timberland = InitialAssessment.objects.filter(classification = 'T').count()
            mineral =InitialAssessment.objects.filter(classification = 'M').count()

            data = total_tax_dec
            data['residential'] = residential
            data['agricultural'] = agricultural
            data['commercial'] = commercial
            data['industrial'] = industrial
            data['special'] = special
            data['timberland'] = timberland
            data['mineral'] = mineral
            data['announcement'] = announcement_serializer.data
            status = ok
            message= 'Success'
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        else:
            status = bad_request
            message= 'Invalid Data'
            errors = announcement_serializer.errors
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
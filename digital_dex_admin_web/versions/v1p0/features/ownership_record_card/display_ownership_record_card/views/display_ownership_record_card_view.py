from rest_framework.views import APIView
from .......models.ownership_record_model import OwnsershipRecordCardModel
from ..serializers.display_ownership_record_card_serializer import DisplayOwnershipRecordCardSerializer
from rest_framework.response import Response
################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class DisplayOwnershipRecordCardViews(APIView):

    def get(self, request, *args, **kwargs):
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
            id = request.query_params["id"]
            tax = OwnsershipRecordCardModel.objects.filter(id = id).first()

            if tax is None:
                message = 'Ownership Record Card does not exist'
                status = not_found
                return Response({"status": status , "message": message , "data": data, "errors":errors})

            serializer = DisplayOwnershipRecordCardSerializer(tax)
        except:
            tax = OwnsershipRecordCardModel.objects.all()
            serializer = DisplayOwnershipRecordCardSerializer(tax,many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message , "data": data, "errors":errors})
from rest_framework.views import APIView
from .......models.tax_map_control_model import TaxMapControl
from ..serializers.display_tax_map_control_serializer import DisplayTaxMapControlSerializer
from rest_framework.response import Response

################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class DisplayTaxMapControlViews(APIView):

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
            tax = TaxMapControl.objects.filter(id = id).first()

            if tax is None:
                message = 'Tax Map Control does not exist'
                status = not_found
                return Response({"status": status , "message": message , "data": data, "errors":errors})

            serializer = DisplayTaxMapControlSerializer(tax)
        except:
            tax = TaxMapControl.objects.all()
            serializer = DisplayTaxMapControlSerializer(tax,many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message , "data": data, "errors":errors})
from rest_framework.views import APIView
from .......models.exempt_assessment_roll_model import ExemptAssessmentRoll
from ..serializers.display_exempt_assessment_serializer import DisplayExemptAssessmentSerializer
from rest_framework.response import Response
################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class DisplayExemptAssessmentRollViews(APIView):

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
            tax = ExemptAssessmentRoll.objects.filter(id = id).first()

            if tax is None:
                message = 'Exempt Assessment Roll does not exist'
                status = not_found
                return Response({"status": status , "message": message , "data": data, "errors":errors})
            serializer = DisplayExemptAssessmentSerializer(tax)
        except:
            tax = ExemptAssessmentRoll.objects.all()
            serializer = DisplayExemptAssessmentSerializer(tax,many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message , "data": data, "errors":errors})
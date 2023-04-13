from rest_framework.views import APIView
from .......models.exempt_assessment_roll_model import ExemptAssessmentRoll
from ..serializers.display_exempt_assessment_serializer import DisplayTaxMapControlSerializer
from rest_framework.response import Response
from constants.http_messages import *

class DisplayExemptAssessmentRollViews(APIView):

    def get(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None

        # if not request.user.is_authenticated:
        #     message = 'You are not logged in'
        #     status = unauthorized
        #     return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        
        try: 
            id = request.query_params["id"]
            tax = ExemptAssessmentRoll.objects.filter(id = id).first()

            if tax is None:
                message = 'Exempt Assessment Roll does not exist'
                status = not_Found
                return Response({"status": status , "message": message , "data": data, "errors":errors})

            serializer = DisplayTaxMapControlSerializer(tax)
        except:
            tax = ExemptAssessmentRoll.objects.all()
            serializer = DisplayTaxMapControlSerializer(tax,many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message , "data": data, "errors":errors})
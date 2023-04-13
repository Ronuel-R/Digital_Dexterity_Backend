from rest_framework.views import APIView
from .......models.taxable_assessment_roll_model import TaxableAssessmentRoll
from ..serializers.display_taxable_assessment_roll_serializer import DisplayTaxAssessmentRollSerializer
from rest_framework.response import Response
from constants.http_messages import *

class DisplayTaxAssessmentRollViews(APIView):

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
            tax = TaxableAssessmentRoll.objects.filter(id = id).first()

            if tax is None:
                message = 'Tax Assessment Roll does not exist'
                status = not_Found
                return Response({"status": status , "message": message , "data": data, "errors":errors})

            serializer = DisplayTaxAssessmentRollSerializer(tax)
        except:
            tax = TaxableAssessmentRoll.objects.all()
            serializer = DisplayTaxAssessmentRollSerializer(tax,many=True)

        data = serializer.data
        message = 'Success'
        status = ok
        return Response({"status": status , "message": message , "data": data, "errors":errors})
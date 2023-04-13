from rest_framework.views import APIView
from .......models.taxable_assessment_roll_model import TaxableAssessmentRoll
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from constants.http_messages import *

class DeleteTaxableAssessmentRollViews(APIView):

    def post(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None

        # if not request.user.is_authenticated:
        #     message = 'You are not logged in'
        #     status = unauthorized
        #     return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        
        if "id" in request.query_params:
            id = request.query_params["id"]
            try:
                tax_model = TaxableAssessmentRoll.objects.get(id=id)
            except ObjectDoesNotExist:
                message = 'Tax Assessment Roll with id {} does not exist'.format(id)
                status = bad_request
                return Response({"status": status, "message": message, "data": data, "errors": errors})
            
            tax_model.delete()

            message = 'Successfuly Deleted'
            status = ok
        else:
            message = 'Invalid Format'
            status = bad_request
        return Response({"status": status , "message": message , "data": data, "errors":errors})
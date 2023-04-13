from rest_framework.views import APIView

################### Models ##########################
from .......models.tax_form_model import TaxForm
################### Static Modules ######################

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from constants.http_messages import *

class DeleteTaxDecViews(APIView):

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
                tax_model = TaxForm.objects.get(id=id)
            except ObjectDoesNotExist:
                message = 'TaxForm with id {} does not exist'.format(id)
                status_code = bad_request
                return Response({"status": status_code, "message": message, "data": data, "errors": errors})
            
            tax_model.delete()

            message = 'Successfuly Deleted'
            status = ok
        else:
            message = 'Invalid Format'
            status = bad_request
        return Response({"status": status , "message": message , "data": data, "errors":errors})
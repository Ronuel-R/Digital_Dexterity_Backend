from rest_framework.views import APIView

################### Models ##########################
from ......models.tax_form_model import TaxForm
from ......models.tax_initial_assessment_model import InitialAssessment

################### Serializer ##########################

from ..serializers.update_tax_serializer import UpdateTaxFormSerializer

################### Static Modules ######################

from django.utils import timezone
from rest_framework.response import Response
from constants.http_messages import *
from constants.update_tax_form_helper import UpdateTaxFormHelper


class UpdateTaxFormViews(APIView):
    
    def put(self, request, *args, **kwargs):
        errors = {}
        data = {}
        status = None
        message = None

        if not request.user.is_authenticated:
            message = 'You are not logged in'
            status = unauthorized
            return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        
        errors = UpdateTaxFormHelper.validate_fields(self, request)

        if len(errors) != 0:
            status = bad_request
            message = 'Invalid Input'
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        id = request.query_params["id"]

        tax_id = TaxForm.objects.filter(id = id).first()

        serializer = UpdateTaxFormSerializer(tax_id, data=request.data, partial = True)
       
        if serializer.is_valid():
            serializer.save()
            
            status = ok
            message = 'Successfuly Registered Tax Declaration'
            data = serializer.data
            errors = serializer.errors
        else:
            status = ok
            message = 'Invalid Value'
            errors = serializer.errors
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
from rest_framework.views import APIView

################### Models ##########################
from ......models.tax_form_model import TaxForm
from ......models.tax_initial_assessment_model import InitialAssessment

################### Serializer ##########################

from ..serializers.update_tax_serializer import UpdateTaxFormSerializer,UpdateInitialAssessmentSerializer

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
        update_serializer = UpdateTaxFormSerializer(tax_id, data=request.data)
        initial_assessment_serializer = UpdateInitialAssessmentSerializer(data = request.data['initial_assessments'],many=True)

        if update_serializer.is_valid() and initial_assessment_serializer.is_valid():

            for initial_assessment in request.data['initial_assessments']:
                update_serializer.save()
                tax_form_obj = TaxForm.objects.get(id = id)
                if initial_assessment['action'] == 'add':
                    ############### Add New Assessment ##################
                    InitialAssessment.objects.create(

                        tax_form = tax_form_obj,
                        classification = initial_assessment['classification'],
                        area = initial_assessment['area'],
                        market_value = initial_assessment['market_value'],
                        actual_use = initial_assessment['actual_use'],
                        assessment_level = initial_assessment['assessment_level'],
                        assessed_value = initial_assessment['assessed_value'],
                    )
                elif initial_assessment['action'] == 'update':

                    initial_assessment_id = initial_assessment['assessment_id']
                    initial_assessment_obj = InitialAssessment.objects.get(id = initial_assessment_id)

                    ################### Update Initial Assessment ###################
                    initial_assessment_obj.tax_form = tax_form_obj,
                    initial_assessment_obj.classification = initial_assessment['classification'],
                    initial_assessment_obj.area = initial_assessment['area'],
                    initial_assessment_obj.market_value = initial_assessment['market_value'],
                    initial_assessment_obj.actual_use = initial_assessment['actual_use'],
                    initial_assessment_obj.assessment_level = initial_assessment['assessment_level'],
                    initial_assessment_obj.assessed_value = initial_assessment['assessed_value'],

                    initial_assessment_obj.save()

                elif initial_assessment['action'] == '':
                    status = ok
                    message = 'Invalid Value'
                    errors = None
                    return Response({"status": status , "message": message ,  "data": data , "errors": errors})

            status = ok
            message = 'Successfuly Registered Tax Declaration'
            data = None
            errors = None
        else:
            status = ok
            message = 'Invalid Value'
            errors = None
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
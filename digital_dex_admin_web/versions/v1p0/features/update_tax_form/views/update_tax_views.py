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
        data = {}
        status_code = None
        message = None
        errors = {}

        try:
            id = request.query_params['id']
            tax_id = TaxForm.objects.get(id=id)
        except TaxForm.DoesNotExist:
            message = 'Tax Form instance does not exist'
            status_code = bad_request
            return Response({"status_code": status_code, "message": message, "errors": errors})

        serializer = UpdateTaxFormSerializer(instance=tax_id, data=request.data)
        if serializer.is_valid():
            initial_assessment = serializer.save()
           
            for validated_initial_assessment in request.data['initial_assessments']:
                initial_assessment_id = validated_initial_assessment.get('id')
                if initial_assessment_id:
                    try:
                        assessment = InitialAssessment.objects.get(pk=initial_assessment_id)
                        assessment_serializer = UpdateInitialAssessmentSerializer(instance=assessment, data=validated_initial_assessment)
                        if assessment_serializer.is_valid():
                            assessment_serializer.save()
                        else:
                            errors.update(assessment_serializer.errors)
                    except InitialAssessment.DoesNotExist:
                        pass
                else:
                    assessment_serializer = UpdateInitialAssessmentSerializer(data=validated_initial_assessment)
                    if assessment_serializer.is_valid():
                        assessment_serializer.save(initial_assessment=initial_assessment)
                    else:
                        errors.update(assessment_serializer.errors)

            status_code = ok
            message = 'Successfully updated Tax Form'
            data = serializer.data
        else:
            status_code = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status_code": status_code, "message": message, "data": data, "errors": errors})
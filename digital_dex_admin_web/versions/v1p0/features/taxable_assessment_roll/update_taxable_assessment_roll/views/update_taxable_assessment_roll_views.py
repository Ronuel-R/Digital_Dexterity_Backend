from rest_framework.response import Response
from rest_framework.views import APIView
from .......models.taxable_assessment_roll_model import TaxableAssessmentRoll
from .......models.taxable_assessment_model import TaxableAssessment
from constants.http_messages import *
from ..serializers.updata_assessment_serializer import UpdateAssessmentSerializer
from ..serializers.update_taxable_assessment_roll_serializer import UpdateTaxAssessmentRollSerializer


class UpdateTaxAssessmentRollView(APIView):
    def put(self, request, *args, **kwargs):
        data = {}
        status_code = None
        message = None
        errors = {}

        try:
            id = request.query_params['id']
            tax_assessment_roll = TaxableAssessmentRoll.objects.get(id=id)
        except TaxableAssessmentRoll.DoesNotExist:
            message = 'Tax Assessment Roll instance does not exist'
            status_code = bad_request
            return Response({"status_code": status_code, "message": message, "errors": errors})

        serializer = UpdateTaxAssessmentRollSerializer(instance=tax_assessment_roll, data=request.data)
        if serializer.is_valid():
            serializer.save()
           
            for validated_assessment in request.data['taxable_assessments']:
                assessment_id = validated_assessment.get('id')
                if assessment_id:
                    try:
                        assessment = TaxableAssessment.objects.get(pk=assessment_id)
                        assessment_serializer = UpdateAssessmentSerializer(instance=assessment, data=validated_assessment)
                        if assessment_serializer.is_valid():
                            assessment_serializer.save()
                        else:
                            errors.update(assessment_serializer.errors)
                    except TaxableAssessment.DoesNotExist:
                        pass
                else:
                    assessment_serializer = UpdateAssessmentSerializer(data=validated_assessment)
                    if assessment_serializer.is_valid():
                        assessment_serializer.save(tax_assessment_roll = tax_assessment_roll)
                    else:
                        errors.update(assessment_serializer.errors)

            status_code = ok
            message = 'Successfully updated Tax Assessment Roll'
            data = serializer.data
        else:
            status_code = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status_code": status_code, "message": message, "data": data, "errors": errors})
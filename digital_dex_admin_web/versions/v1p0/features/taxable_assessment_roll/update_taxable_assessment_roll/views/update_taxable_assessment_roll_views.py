from rest_framework.response import Response
from rest_framework.views import APIView
from .......models.taxable_assessment_roll_model import TaxableAssessmentRoll
from .......models.taxable_assessment_model import TaxableAssessment
from ..serializers.update_assessment_serializer import UpdateAssessmentSerializer
from ..serializers.update_taxable_assessment_roll_serializer import UpdateTaxAssessmentRollSerializer
from django.utils import timezone
################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class UpdateTaxAssessmentRollView(APIView):
    def put(self, request, *args, **kwargs):
        data = {}
        status = None
        message = None
        errors = {}
        
        # token = AuthUser.get_token(request)

        # if type(token) == dict:
        #     return Response(token)

        # payload = AuthUser.get_user(token)

        # if 'errors' in payload:
        #     return Response(payload)

        # errors = PermissionChecker.validate_permission_edit(payload['position_level'])

        # if len(errors) != 0:
        #     status = bad_request
        #     message = 'Invalid Input'
        #     return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        try:
            id = request.query_params['id']
            tax_assessment_roll = TaxableAssessmentRoll.objects.get(id=id)
        except TaxableAssessmentRoll.DoesNotExist:
            message = 'Tax Assessment Roll does not exist'
            status = bad_request
            return Response({"status": status, "message": message, "errors": errors})
        tax_assessment_roll.date_modified = timezone.now().date()
        serializer = UpdateTaxAssessmentRollSerializer(instance=tax_assessment_roll, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
           
            for validated_assessment in request.data['taxable_assessments']:
                assessment_id = validated_assessment.get('id')
                if assessment_id:
                    try:
                        assessment = TaxableAssessment.objects.get(pk=assessment_id)
                        assessment_serializer = UpdateAssessmentSerializer(instance=assessment, data=validated_assessment,partial=True)
                        if assessment_serializer.is_valid():
                            assessment_serializer.save()
                        else:
                            errors.update(assessment_serializer.errors)
                    except TaxableAssessment.DoesNotExist:
                        pass
                else:
                    assessment_serializer = UpdateAssessmentSerializer(data=validated_assessment,partial=True)
                    if assessment_serializer.is_valid():
                        assessment_serializer.save(tax_assessment_roll = tax_assessment_roll)
                    else:
                        errors.update(assessment_serializer.errors)

            status = ok
            message = 'Successfully updated Tax Assessment Roll'
            data = serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status": status, "message": message, "data": data, "errors": errors})
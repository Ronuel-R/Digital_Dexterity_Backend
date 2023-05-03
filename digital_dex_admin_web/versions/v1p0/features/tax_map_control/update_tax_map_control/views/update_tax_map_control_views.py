from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .......models.tax_map_control_model import TaxMapControl
from .......models.assessment_model import Assessment
from ..serializers.update_tax_map_control_serializer import UpdateTaxMapControlSerializer
from ..serializers.assessment_serializer import UpdateAssessmentSerializer
from django.utils import timezone

################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class UpdateTaxMapControl(APIView):
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

        # errors = PermissionChecker.validate_permission_edit(self,payload)

        # if len(errors) != 0:
        #     status = bad_request
        #     message = 'Invalid Input'
        #     return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        try:
            id = request.query_params['id']
            tax_map_control = TaxMapControl.objects.get(id=id)
        except TaxMapControl.DoesNotExist:
            message = 'Tax Map Control does not exist'
            status = bad_request
            return Response({"status": status, "message": message, "errors": errors})
        tax_map_control.date_modified = timezone.now()
        serializer = UpdateTaxMapControlSerializer(instance=tax_map_control, data=request.data,partial=True)
        if serializer.is_valid():
            tax_map_control = serializer.save()

            for validated_assessment in request.data['assessments']:
                assessment_id = validated_assessment.get('id')
                if assessment_id:
                    try:
                        assessment = Assessment.objects.get(pk=assessment_id)
                        assessment_serializer = UpdateAssessmentSerializer(instance=assessment, data=validated_assessment,partial=True)
                        if assessment_serializer.is_valid():
                            assessment_serializer.save()
                        else:
                            errors.update(assessment_serializer.errors)
                    except Assessment.DoesNotExist:
                        pass
                else:
                    assessment_serializer = UpdateAssessmentSerializer(data=validated_assessment,partial=True)
                    if assessment_serializer.is_valid():
                        assessment_serializer.save(tax_map_control=tax_map_control)
                    else:
                        errors.update(assessment_serializer.errors)

            status = ok
            message = 'Successfully updated Tax Map Control'
            data = serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status": status, "message": message, "data": data, "errors": errors})

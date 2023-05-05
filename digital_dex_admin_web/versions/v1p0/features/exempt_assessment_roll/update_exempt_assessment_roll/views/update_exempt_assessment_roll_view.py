from rest_framework.response import Response
from rest_framework.views import APIView
from .......models.exempt_assessment_roll_model import ExemptAssessmentRoll
from .......models.exempt_assessment_model import ExemptAssessment
from ..serializers.update_exempt_assessment_serializer import UpdateExemptAssessmentRollSerializer
from ..serializers.exempt_assessment_serializer import UpdateAssessmentSerializer
from django.utils import timezone

################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class UpdateExemptAssessmentRollView(APIView):
    def put(self, request, *args, **kwargs):
        data = {}
        status = None
        message = None
        errors = {}

        token = AuthUser.get_token(request)

        if type(token) == dict:
            return Response(token)

        payload = AuthUser.get_user(token)

        if 'errors' in payload:
            return Response(payload)

        errors = PermissionChecker.validate_permission_edit(self,payload)

        if len(errors) != 0:
            status = bad_request
            message = 'Invalid Input'
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        try:
            id = request.query_params['id']
            exempt_assessment_roll = ExemptAssessmentRoll.objects.get(id=id)
        except ExemptAssessmentRoll.DoesNotExist:
            message = 'Exempt Assessment Roll does not exist'
            status = bad_request
            return Response({"status": status, "message": message, "errors": errors})
        exempt_assessment_roll.date_modified = timezone.now()
        serializer = UpdateExemptAssessmentRollSerializer(instance=exempt_assessment_roll, data=request.data,partial=True)
        if serializer.is_valid():
            exempt_assessment = serializer.save()
            for validated_assessment in request.data['exempt_assessments']:
                assessment_id = validated_assessment.get('id')
                if assessment_id:
                    try:
                        assessment = ExemptAssessment.objects.get(pk=assessment_id)
                        assessment_serializer = UpdateAssessmentSerializer(instance=assessment, data=validated_assessment,partial=True)
                        if assessment_serializer.is_valid():
                            assessment_serializer.save()
                        else:
                            errors.update(assessment_serializer.errors)
                    except ExemptAssessment.DoesNotExist:
                        pass
                else:
                    assessment_serializer = UpdateAssessmentSerializer(data=validated_assessment,partial=True)
                    if assessment_serializer.is_valid():
                        assessment_serializer.save(exempt_assessment_roll=exempt_assessment)
                    else:
                        errors.update(assessment_serializer.errors)

            status = ok
            message = 'Successfully updated Exempt Assessment Roll'
            data = serializer.data
            exempt_assessment_roll = ExemptAssessmentRoll.objects.get(id=id)
            data['exempt_assessments'] = UpdateAssessmentSerializer(exempt_assessment_roll.exemptassessment_set.all(),many=True).data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status": status, "message": message, "data": data, "errors": errors})
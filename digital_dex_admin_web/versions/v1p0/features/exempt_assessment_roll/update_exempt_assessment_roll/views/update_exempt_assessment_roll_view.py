from rest_framework.response import Response
from rest_framework.views import APIView
from .......models.exempt_assessment_roll_model import ExemptAssessmentRoll
from .......models.exempt_assessment_model import ExemptAssessment
from constants.http_messages import *
from ..serializers.update_exempt_assessment_serializer import UpdateExemptAssessmentRollSerializer
from ..serializers.exempt_assessment_serializer import UpdateAssessmentSerializer
from django.utils import timezone

class UpdateExemptAssessmentRollView(APIView):
    def put(self, request, *args, **kwargs):
        data = {}
        status = None
        message = None
        errors = {}

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
                        assessment_serializer.save(exempt_map_control=exempt_assessment_roll)
                    else:
                        errors.update(assessment_serializer.errors)
            serializer.save()
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
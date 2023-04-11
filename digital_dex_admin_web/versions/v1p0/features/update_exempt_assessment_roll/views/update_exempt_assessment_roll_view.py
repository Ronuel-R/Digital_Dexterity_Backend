from rest_framework.response import Response
from rest_framework.views import APIView
from ......models.exempt_assessment_roll_model import ExemptAssessmentRoll
from ......models.exempt_assessment_model import ExemptAssessment
from constants.http_messages import *
from ..serializers.update_exempt_assessment_serializer import UpdateExemptAssessmentRollSerializer
from ..serializers.exempt_assessment_serializer import UpdateAssessmentSerializer


class UpdateExemptAssessmentRollView(APIView):
    def put(self, request, *args, **kwargs):
        data = {}
        status_code = None
        message = None
        errors = {}

        try:
            id = request.query_params['id']
            exempt_assessment_roll = ExemptAssessmentRoll.objects.get(id=id)
        except ExemptAssessmentRoll.DoesNotExist:
            message = 'Exempt Assessment Roll instance does not exist'
            status_code = bad_request
            return Response({"status_code": status_code, "message": message, "errors": errors})

        serializer = UpdateExemptAssessmentRollSerializer(instance=exempt_assessment_roll, data=request.data)
        if serializer.is_valid():
            serializer.save()
           
            for validated_assessment in request.data['exempt_assessments']:
                assessment_id = validated_assessment.get('id')
                if assessment_id:
                    try:
                        assessment = ExemptAssessment.objects.get(pk=assessment_id)
                        assessment_serializer = UpdateAssessmentSerializer(instance=assessment, data=validated_assessment)
                        if assessment_serializer.is_valid():
                            assessment_serializer.save()
                        else:
                            errors.update(assessment_serializer.errors)
                    except ExemptAssessment.DoesNotExist:
                        pass
                else:
                    assessment_serializer = UpdateAssessmentSerializer(data=validated_assessment)
                    if assessment_serializer.is_valid():
                        assessment_serializer.save(exempt_map_control=exempt_assessment_roll)
                    else:
                        errors.update(assessment_serializer.errors)

            status_code = ok
            message = 'Successfully updated Tax Map Control'
            data = serializer.data
        else:
            status_code = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status_code": status_code, "message": message, "data": data, "errors": errors})
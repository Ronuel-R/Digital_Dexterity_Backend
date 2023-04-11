from rest_framework.response import Response
from rest_framework.views import APIView
from ......models.ownership_record_model import OwnsershipRecordCardModel
from ......models.record_model import RecordCardModel
from constants.http_messages import *
from ..serializers.update_ownership_record_card_serializer import UpdateOwnershipRecordCardSerializer
from ..serializers.update_records_serializer import UpdateRecordSerializer


class UpdateOwnershipRecordCardView(APIView):
    def put(self, request, *args, **kwargs):
        data = {}
        status_code = None
        message = None
        errors = {}

        try:
            if 'id' in request.query_params:
                id = request.query_params['id']
                exempt_assessment_roll = OwnsershipRecordCardModel.objects.get(id=id)
            else:
                message = 'ID is not provided'
                status_code = bad_request
                return Response({"status_code": status_code, "message": message, "errors": errors})
        except OwnsershipRecordCardModel.DoesNotExist:
            message = 'Exempt Assessment Roll instance does not exist'
            status_code = bad_request
            return Response({"status_code": status_code, "message": message, "errors": errors})

        serializer = UpdateOwnershipRecordCardSerializer(instance=exempt_assessment_roll, data=request.data)
        if serializer.is_valid():
            serializer.save()
           
            for validated_records in request.data['records']:
                assessment_id = validated_records.get('id')
                if assessment_id:
                    try:
                        assessment = RecordCardModel.objects.get(pk=assessment_id)
                        assessment_serializer = UpdateRecordSerializer(instance=assessment, data=validated_records)
                        if assessment_serializer.is_valid():
                            assessment_serializer.save()
                        else:
                            errors.update(assessment_serializer.errors)
                    except RecordCardModel.DoesNotExist:
                        pass
                else:
                    assessment_serializer = UpdateRecordSerializer(data=validated_records)
                    if assessment_serializer.is_valid():
                        assessment_serializer.save(exempt_map_control=exempt_assessment_roll)
                    else:
                        errors.update(assessment_serializer.errors)

            status_code = ok
            message = 'Successfully updated Ownership Record Card'
            data = serializer.data
        else:
            status_code = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status_code": status_code, "message": message, "data": data, "errors": errors})
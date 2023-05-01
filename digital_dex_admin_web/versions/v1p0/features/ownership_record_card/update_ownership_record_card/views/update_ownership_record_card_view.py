from rest_framework.response import Response
from rest_framework.views import APIView
from .......models.ownership_record_model import OwnsershipRecordCardModel
from .......models.record_model import RecordCardModel
from ..serializers.update_ownership_record_card_serializer import UpdateOwnershipRecordCardSerializer
from ..serializers.update_records_serializer import UpdateRecordSerializer
from django.utils import timezone
################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *
class UpdateOwnershipRecordCardView(APIView):
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
            if 'id' in request.query_params:
                id = request.query_params['id']
                ownership_record = OwnsershipRecordCardModel.objects.get(id=id)
            else:
                message = 'ID is not provided'
                status = bad_request
                return Response({"status": status, "message": message, "errors": errors})
        except OwnsershipRecordCardModel.DoesNotExist:
            message = 'Exempt Assessment Roll instance does not exist'
            status = bad_request
            return Response({"status": status, "message": message, "errors": errors})
        
        ownership_record.modified = timezone.now().date()
        serializer = UpdateOwnershipRecordCardSerializer(instance=ownership_record, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
           
            for validated_records in request.data['records']:
                assessment_id = validated_records.get('id')
                if assessment_id:
                    try:
                        assessment = RecordCardModel.objects.get(pk=assessment_id)
                        assessment_serializer = UpdateRecordSerializer(instance=assessment, data=validated_records,partial=True)
                        if assessment_serializer.is_valid():
                            assessment_serializer.save()
                        else:
                            errors.update(assessment_serializer.errors)
                    except RecordCardModel.DoesNotExist:
                        pass
                else:
                    assessment_serializer = UpdateRecordSerializer(data=validated_records,partial=True)
                    if assessment_serializer.is_valid():
                        assessment_serializer.save(exempt_map_control=ownership_record)
                    else:
                        errors.update(assessment_serializer.errors)

            status = ok
            message = 'Successfully updated Ownership Record Card'
            data = serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

        return Response({"status": status, "message": message, "data": data, "errors": errors})
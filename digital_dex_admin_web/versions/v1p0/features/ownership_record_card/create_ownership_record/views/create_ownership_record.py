############## Constants ###############
from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from django.utils import timezone
############## From Features #############
from .......models.record_model import RecordCardModel
from .......models.ownership_record_model import OwnsershipRecordCardModel
from ..serializers.create_ownership_record_serializer import OwnershipRecordSerializer
from ..serializers.create_record_serializer import RecordSerializer
############## Helper ################
# from constants.create_tax_map_control_helper import TaxMapControlHelper

class OwnershipRecordCardView(APIView):
    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        # if not request.user.is_authenticated:
        #     message = 'You are not logged in'
        #     status = unauthorized
        #     return Response({"status": status , "message": message ,  "data": data , "errors":errors})
        
        # errors = TaxMapControlHelper.validate_fields(self, request)

        # if len(errors) != 0:
        #     status = bad_request
        #     message = 'Invalid Input'
        #     return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        serializer = OwnershipRecordSerializer(data=request.data)

        if serializer.is_valid():
            create_ownership_record_card_obj = OwnsershipRecordCardModel.objects.create(
                name_of_owner = request.data['name_of_owner'],
                address = request.data['address'],
                tel_no = request.data['tel_no'],
                tin = request.data['tin'],
                date_prepared = request.data['date_prepared'],
                prov_city_mun = request.data['prov_city_mun'],
                index_no = request.data['index_no'],
                modified = timezone.now(),
            )
            create_ownership_record_card_obj.save()

            assessment_serializer = RecordSerializer(data=request.data['records'], many=True)

            if assessment_serializer.is_valid():
                for validated_records in request.data['records']:
                    RecordCardModel.objects.create(
                        ownership = create_ownership_record_card_obj,
                        date_of_entry = validated_records['date_of_entry'],
                        kind = validated_records['kind'],
                        class_code = validated_records['class_code'],
                        pin = validated_records['pin'],
                        title_no = validated_records['title_no'],
                        lot_block_no = validated_records['lot_block_no'],
                        arp_no = validated_records['arp_no'],
                        td_no = validated_records['td_no'],
                        previous_owner = validated_records['previous_owner'],
                        location_of_property = validated_records['location_of_property'],
                        area = validated_records['area'],
                        market_value = validated_records['market_value'],
                        assessed_value = validated_records['assessed_value'],
                        remarks = validated_records['remarks']
                    )
                    
            if len(serializer.errors) != 0:
                errors['ownership_record'] = serializer.errors

            if len(assessment_serializer.errors) != 0:
                errors['records'] =  assessment_serializer.errors
                
            status = created
            message = 'Successfully Created Ownership Record Card'
            data = serializer.data
            data['records'] = assessment_serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        return Response({"status": status , "message": message ,  "data": data , "errors": errors})  
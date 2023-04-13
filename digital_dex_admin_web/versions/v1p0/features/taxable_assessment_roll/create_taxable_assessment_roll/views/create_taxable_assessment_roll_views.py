############## Constants ###############
from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from django.utils import timezone
############## From Features #############
from .......models.taxable_assessment_roll_model import TaxableAssessmentRoll
from .......models.taxable_assessment_model import TaxableAssessment
from ..serializers.create_taxable_assessment_roll_serializer import TaxAssessmentRollSerializer
from ..serializers.create_assessment_serializer import AssessmentSerializer
############## Helper ################
# from constants.create_tax_map_control_helper import TaxMapControlHelper

class CreateTaxableAssessmentRollView(APIView):
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

        serializer = TaxAssessmentRollSerializer(data=request.data)

        if serializer.is_valid():
            create_tax_assessment_roll_obj = TaxableAssessmentRoll.objects.create(
                prov_city = request.data['prov_city'],
                prov_city_index_no = request.data['prov_city_index_no'],
                mun_city = request.data['mun_city'],
                mun_city_index_no = request.data['mun_city_index_no'],
                barangay = request.data['barangay'],
                barangay_index_no = request.data['barangay_index_no'],
                section_index_no = request.data['section_index_no'],
                modified = timezone.now(),
            )
            create_tax_assessment_roll_obj.save()

            assessment_serializer = AssessmentSerializer(data=request.data['taxable_assessments'], many=True)

            if assessment_serializer.is_valid():
                for validated_tax_assessment in request.data['taxable_assessments']:
                   TaxableAssessment.objects.create(
                        tax_assessment_roll = create_tax_assessment_roll_obj,
                        arpn = validated_tax_assessment['arpn'],
                        td_no = validated_tax_assessment['td_no'],
                        pin = validated_tax_assessment['pin'],
                        lot_block_no = validated_tax_assessment['lot_block_no'],
                        property_owner = validated_tax_assessment['property_owner'],
                        address_of_property_owner = validated_tax_assessment['address_of_property_owner'],
                        kind = validated_tax_assessment['kind'],
                        classification = validated_tax_assessment['classification'],
                        assessed_value = validated_tax_assessment['assessed_value'],
                        prev_arpn = validated_tax_assessment['prev_arpn'],
                        prev_td_no = validated_tax_assessment['prev_td_no'],
                        effectivity = validated_tax_assessment['effectivity'],
                        remarks = validated_tax_assessment['remarks']
                    )
                    
            if len(serializer.errors) != 0:
                errors['tax_assessment_roll'] = serializer.errors

            if len(assessment_serializer.errors) != 0:
                errors['assessments'] =  assessment_serializer.errors
                
            status = created
            message = 'Successfully Created Tax Assessment Roll'
            data = serializer.data
            data['assessments'] = assessment_serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        return Response({"status": status , "message": message ,  "data": data , "errors": errors})  
from rest_framework.views import APIView
from rest_framework.response import Response
from .......models.assessment_model import Assessment
from .......models.tax_map_control_model import TaxMapControl
from ..serializers.create_tax_map_control_serializer import CreateTaxMapControlSerializer
from ..serializers.assessment_serializer import AssessmentSerializer
from constants.create_tax_map_control_helper import TaxMapControlHelper
from django.utils import timezone

################### Consants #####################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *

class CreateTaxMapControlViews(APIView):
    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        # token = AuthUser.get_token(request)

        # if type(token) == dict:
        #     return Response(token)

        # payload = AuthUser.get_user(token)

        # if 'errors' in payload:
        #     return Response(payload)
        
        # errors = TaxMapControlHelper.validate_fields(self, request)

        # if len(errors) != 0:
        #     status = bad_request
        #     message = 'Invalid Input'
        #     return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        serializer = CreateTaxMapControlSerializer(data=request.data)

        if serializer.is_valid():
            create_tax_map_control_obj = TaxMapControl.objects.create(
                prov_city = request.data['prov_city'],
                prov_city_index_no = request.data['prov_city_index_no'],
                mun_city = request.data['mun_city'],
                mun_city_index_no = request.data['mun_city_index_no'],
                barangay = request.data['barangay'],
                barangay_index_no = request.data['barangay_index_no'],
                section_index_no = request.data['section_index_no'],
                date_modified = timezone.now()
            )
            create_tax_map_control_obj.save()

            assessment_serializer = AssessmentSerializer(data=request.data['assessments'], many=True)

            if assessment_serializer.is_valid():
                for validated_assessment in request.data['assessments']:
                    Assessment.objects.create(
                        tax_map_control=create_tax_map_control_obj,
                        assessors_lot_no=validated_assessment['assessors_lot_no'],
                        survey_lot_no=validated_assessment['survey_lot_no'],
                        land_title_no=validated_assessment['land_title_no'],
                        land_area=validated_assessment['land_area'],
                        land_class_code=validated_assessment['land_class_code'],
                        name_of_owner=validated_assessment['name_of_owner'],
                        arp_no=validated_assessment['arp_no'],
                        td_no=validated_assessment['td_no'],
                        building_structure=validated_assessment['building_structure'],
                        machinery=validated_assessment['machinery'],
                        others=validated_assessment['others'],
                        remarks=validated_assessment['remarks']
                    )
            if len(serializer.errors) != 0:
                errors['tax_map_control'] = serializer.errors

            if len(assessment_serializer.errors) != 0:
                errors['assessments'] =  assessment_serializer.errors
                
            status = created
            message = 'Successfully Created Tax Map Control'
            data = serializer.data
            data['assessments'] = assessment_serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        
        return Response({"status": status , "message": message ,  "data": data , "errors": errors})  
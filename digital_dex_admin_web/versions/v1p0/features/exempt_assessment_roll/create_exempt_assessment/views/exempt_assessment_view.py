############## Constants ###############
from rest_framework.views import APIView
from rest_framework.response import Response
from constants.http_messages import *
from django.utils import timezone
############## From Features #############
from .......models.exempt_assessment_model import ExemptAssessment
from .......models.exempt_assessment_roll_model import ExemptAssessmentRoll
from ..serializers.exempt_assessment_serializer import ExemptAssessmentRollSerializer
from ..serializers.assessment_serializer import AssessmentSerializer
############## Helper ################
from constants.auth_user import AuthUser
from constants.permission_checker_helper import PermissionChecker
from constants.http_messages import *
from constants.create_tax_map_control_helper import TaxMapControlHelper

class ExemptAssessmentRollView(APIView):
    def post(self, request):
        errors = {}
        data = {}
        status = None
        message = None

        token = AuthUser.get_token(request)

        if type(token) == dict:
            return Response(token)

        payload = AuthUser.get_user(token)

        if 'errors' in payload:
            return Response(payload)

        # errors = TaxMapControlHelper.validate_fields(self, request)

        # if len(errors) != 0:
        #     status = bad_request
        #     message = 'Invalid Input'
        #     return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        serializer = ExemptAssessmentRollSerializer(data=request.data)

        if serializer.is_valid():
            create_exempt_assessment_roll_obj = ExemptAssessmentRoll.objects.create(
                revision_year = request.data['revision_year'],
                prov_city = request.data['prov_city'],
                prov_city_index_no = request.data['prov_city_index_no'],
                mun_city = request.data['mun_city'],
                mun_city_index_no = request.data['mun_city_index_no'],
                barangay = request.data['barangay'],
                barangay_index_no = request.data['barangay_index_no'],
                section = request.data['section'],
                section_index_no = request.data['section_index_no'],
                date_prepared = request.data['date_prepared'],
                date_modified = timezone.now(),
            )
            create_exempt_assessment_roll_obj.save()

            assessment_serializer = AssessmentSerializer(data=request.data['exempt_assessments'], many=True)

            if assessment_serializer.is_valid():
                for validated_exempt_assessment in request.data['exempt_assessments']:
                    ExemptAssessment.objects.create(
                        exempt_assessment_roll = create_exempt_assessment_roll_obj,
                        arpn = validated_exempt_assessment['arpn'],
                        td_no = validated_exempt_assessment['td_no'],
                        pin = validated_exempt_assessment['pin'],
                        lot_block_no = validated_exempt_assessment['lot_block_no'],
                        property_owner = validated_exempt_assessment['property_owner'],
                        address_of_property_owner = validated_exempt_assessment['address_of_property_owner'],
                        classification = validated_exempt_assessment['classification'],
                        # kind = validated_tax_assessment['kind'],
                        assessed_value = validated_exempt_assessment['assessed_value'],
                        legal_basis = validated_exempt_assessment['legal_basis'],
                        effectivity = validated_exempt_assessment['effectivity'],
                        remarks = validated_exempt_assessment['remarks']
                    )

            if len(serializer.errors) != 0:
                errors['exempt_assessment_roll'] = serializer.errors

            if len(assessment_serializer.errors) != 0:
                errors['assessments'] =  assessment_serializer.errors

            status = created
            message = 'Successfully Created Exempt Assessment Roll'
            data = serializer.data
            data['assessments'] = assessment_serializer.data
        else:
            status = bad_request
            message = 'Invalid Value'
            errors = serializer.errors

            return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        return Response({"status": status , "message": message ,  "data": data , "errors": errors})
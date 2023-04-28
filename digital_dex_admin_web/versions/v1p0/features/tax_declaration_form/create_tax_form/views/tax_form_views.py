from rest_framework.views import APIView

################### Models ##########################
from .......models.tax_form_model import TaxForm
from .......models.tax_initial_assessment_model import InitialAssessment

################### Serializer ##########################

from ..serializers.tax_form_serializer import TaxFormSerializer
from ..serializers.initial_assessment_serializer import InitialAssessmentSerializer

################### Static Modules ######################

from rest_framework.response import Response
from constants.http_messages import *
from constants.auth_user import AuthUser
from constants.tax_form_helper import TaxFormHelper
import jwt
from django.utils import timezone

class TaxFormViews(APIView):
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

        errors = TaxFormHelper.validate_fields(self, request)

        if len(errors) != 0:
            status = bad_request
            message = 'Invalid Input'
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})

        serializer = TaxFormSerializer(data=request.data)

        if serializer.is_valid():
            tax_declaration_form = TaxForm.objects.create(

                td_no = request.data['td_no'],
                property_identification_no = request.data['property_identification_no'],

                ############## OWNER ########################

                owner = request.data['owner'],
                owner_tin = request.data['owner_tin'],
                owner_address = request.data['owner_address'],
                owner_tel_no = request.data['owner_tel_no'],

                ############## Admin ####################

                administrator_beneficial_user = request.data['administrator_beneficial_user'],
                admin_tin = request.data['admin_tin'],
                admin_address = request.data['admin_address'],
                admin_tel_no = request.data['admin_tel_no'],

                ############## PROPERTY ##################

                property_location = request.data['property_location'],
                oct_no = request.data['oct_no'],
                survey_no = request.data['survey_no'],
                cct = request.data['cct'],
                lot_no = request.data['lot_no'],
                dated = request.data['dated'],
                blk_no = request.data['blk_no'],

                ############## BOUNDARY ###################

                north = request.data['north'],
                west = request.data['west'],
                east = request.data['east'],
                south = request.data['south'],

                ############## INITIAL ASSESSMENT ################

                # total_assessed_value = request.data['total_assessed_value'],
                # total_market_value = request.data['total_market_value'],
                total_assessed_value_words = request.data['total_assessed_value_words'],


                ############## KIND OF PROPERTY ############

                property_choices = request.data['property_choices'],

                mach_brief_description = request.data['mach_brief_description'],

                no_of_storeys = request.data['no_of_storeys'],
                brief_description = request.data['brief_description'],

                specify = request.data['specify'],

                ############# FINAL ASSESSMENT ############
                tax_status = request.data['tax_status'],

                ############# EFFECTIVITY OF ASSESSMENT ############

                qtr = request.data['qtr'],
                year = request.data['year'],
                approved_by = request.data['approved_by'],
                date_assessed = request.data['date_assessed'],

                ############# CANCEL OWNERSHIP #####################

                cancels_td_no = request.data['cancels_td_no'],
                cancel_owner = request.data['cancel_owner'],
                cancel_previous_av_php = request.data['cancel_previous_av_php'],
                memoranda = request.data['memoranda'],

                ################## Notes #######################
                sanggunian = request.data['sanggunian'],
                under_ord_num = request.data['under_ord_num'],
                notes_date = request.data['notes_date'],
                date_modified = timezone.now()
            )

            tax_declaration_form.save()
            ############## INITIAL ASSESSMENT ################
            initial_assessment_serializer = InitialAssessmentSerializer(data=request.data['initial_assessments'],many=True)

            if initial_assessment_serializer.is_valid():
                for initial_assessment in request.data['initial_assessments']:
                    InitialAssessment.objects.create(
                        tax_form = tax_declaration_form,
                        classification = initial_assessment['classification'],
                        area = initial_assessment['area'],
                        market_value = initial_assessment['market_value'],
                        actual_use = initial_assessment['actual_use'],
                        assessment_level = initial_assessment['assessment_level'],
                        assessed_value = initial_assessment['assessed_value'],
                    )

            if len(serializer.errors) != 0:
                errors['tax_form'] = serializer.errors
            if len(initial_assessment_serializer.errors) != 0:
                errors['initial_assessment'] =  initial_assessment_serializer.errors

            status = created
            message = 'Successfuly Registered Tax Declaration'
            data = serializer.data
            data['initial_assessment'] = initial_assessment_serializer.data
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        else:
            status = ok
            message = 'Invalid Value'
            errors = serializer.errors
            return Response({"status": status , "message": message ,  "data": data , "errors": errors})
        

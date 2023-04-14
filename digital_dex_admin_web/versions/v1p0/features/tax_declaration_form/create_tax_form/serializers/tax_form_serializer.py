from rest_framework import serializers
from .......models.tax_form_model import TaxForm
from .initial_assessment_serializer import InitialAssessmentSerializer
from datetime import datetime

class TaxFormSerializer(serializers.ModelSerializer):
    # initial_assessments = InitialAssessmentSerializer(many=True, required = True)
    dated = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d'])
    date_assessed = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d'])
    notes_date = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d'])
    no_of_storeys = serializers.IntegerField(required=False)
    brief_description = serializers.CharField(required=False)
    specify = serializers.CharField(required=False)
    property_choices = serializers.ChoiceField(required=False, choices=[(('L', 'Land')),('B', 'Building'), ('M', 'Machinery'), ('O', 'Others')])
    tax_status = serializers.ChoiceField(required=False, choices=[(('T', 'Taxable')),('E', 'Exempt')])
    class Meta:
        model = TaxForm
        fields = ['id','td_no', 'property_identification_no',
                  
                  ############## OWNER ########################
                  'owner', 'owner_tin','owner_address','owner_tel_no',
                  
                  ############## Admin ####################
                  'administrator_beneficial_user', 'admin_tin', 'admin_tel_no',
                  'admin_address',

                  ############## PROPERTY ##################
                  'property_location','oct_no',
                  'survey_no','cct','lot_no','dated','blk_no',

                  ############## BOUNDARY ###################
                  'north','west','east','south',
                  
                  ############## KIND OF PROPERTY ############
                  'property_choices','no_of_storeys','brief_description','specify',

                  ############## INITIAL ASSESSMENT #########
                  # 'initial_assessments',
                  'total_assessed_value',
                  'total_assessed_value_words',
                  'total_market_value',
                  
                  ############# FINAL ASSESSMENT ############
                  'tax_status',

                  ############# EFFECTIVITY OF ASSESSMENT ############
                  'year',
                  'approved_by',
                  'date_assessed',

                  ############# CANCEL OWNERSHIP #####################
                  'cancels_td_no','cancel_owner','cancel_previous_av_php','memoranda',

                  ############# Notes ######################
                  'sanggunian','under_ord_num','notes_date'

                  ]
        
def validate_dated(self, value):
    # Convert the date string to a date object
    date_obj = datetime.strptime(value, '%Y-%m-%d').date()
    # Format the date object as a string in the desired format
    date_str = date_obj.strftime('%Y-%m-%d')
    # Parse the formatted string as a date object
    formatted_date = datetime.strptime(date_str, '%m-%d-%Y').date()
    return formatted_date
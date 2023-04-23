from rest_framework import serializers
from .......models.tax_form_model import TaxForm
from .update_initial_assessment_serializer import UpdateInitialAssessmentSerializer


class UpdateTaxFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxForm
        fields = ['td_no', 'property_identification_no',
                  
                  ############## OWNER ########################
                  'owner', 'owner_tin','owner_address','owner_tel_no',
                  
                  ############## Admin ####################
                  'administrator_beneficial_user', 'admin_tin', 'admin_tel_no',

                  ############## PROPERTY ##################
                  'property_location','oct_no',
                  'survey_no','cct','lot_no','dated','blk_no',
                  ############## BOUNDARY ###################
                  'north','west','east','south',
                  
                  ############## KIND OF PROPERTY ############
                  'property_choices','no_of_storeys','brief_description',

                  ############## INITIAL ASSESSMENT #########
                  'total_assessed_value_words',
                  # 'total_assessed_value',
                  # 'total_market_value',
                  
                  ############# FINAL ASSESSMENT ############
                  'taxable',

                  ############# EFFECTIVITY OF ASSESSMENT ############
                  'year',
                  'approved_by',
                  'date_assessed',

                  ############# CANCEL OWNERSHIP #####################
                  'cancels_td_no','cancel_owner','cancel_previous_av_pph','memoranda'
                  ]
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['initial_assessments'] = UpdateInitialAssessmentSerializer(instance.initialassessment_set.all(),many=True).data
        return rep
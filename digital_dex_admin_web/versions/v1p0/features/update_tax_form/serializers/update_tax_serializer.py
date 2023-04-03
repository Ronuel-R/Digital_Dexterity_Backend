from rest_framework import serializers
from ......models.tax_form_model import TaxForm
from .update_initial_assessment_serializer import UpdateInitialAssessmentSerializer
from ......models.tax_initial_assessment_model import InitialAssessment

class UpdateTaxFormSerializer(serializers.ModelSerializer):
    initial_assessments = UpdateInitialAssessmentSerializer(many=True,read_only=True)
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
                  'initial_assessments',
                  'total_assessed_value',
                  'total_assessed_value_words',
                  'total_market_value',
                  
                  ############# FINAL ASSESSMENT ############
                  'taxable',

                  ############# EFFECTIVITY OF ASSESSMENT ############
                  'year',
                #   'approved_by',
                  'date_assessed',

                  ############# CANCEL OWNERSHIP #####################
                  'cancels_td_no','cancel_owner','cancel_previous_av_pph','memoranda'
                  ]
        
    # def create(self, validated_data):
    #   initial_assessments_data = validated_data.pop('initial_assessments')
    #   tax_form = TaxForm.objects.create(**validated_data)
    #   for initial_assessment_data in initial_assessments_data:
    #       InitialAssessment.objects.create(tax_form=tax_form, **initial_assessment_data)
    #   return tax_form
  
    # def update(self, instance, validated_data):
    #   initial_assessments_data = validated_data.pop('initial_assessments', None)
    #   instance = super().update(instance, validated_data)
    #   if initial_assessments_data is not None:
    #       instance.initial_assessments.all().delete()
    #       for initial_assessment_data in initial_assessments_data:
    #           InitialAssessment.objects.create(tax_form = instance, **initial_assessment_data)
    #   return instance
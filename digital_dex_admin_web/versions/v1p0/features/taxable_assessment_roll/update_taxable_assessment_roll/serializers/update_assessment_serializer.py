from rest_framework import serializers
from .......models.taxable_assessment_model import TaxableAssessment

class UpdateAssessmentSerializer(serializers.ModelSerializer):
    arpn = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    prev_arpn = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    effectivity = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    remarks = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    class Meta:
        model = TaxableAssessment
        fields = ['id','tax_assessment_roll','arpn','td_no','pin','lot_block_no','property_owner',
                  'address_of_property_owner','classification','assessed_value','prev_arpn','prev_td_no','effectivity',
                  'remarks',
                  ]
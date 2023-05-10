from rest_framework import serializers
from .......models.exempt_assessment_model import ExemptAssessment

class UpdateAssessmentSerializer(serializers.ModelSerializer):
    arpn = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    effectivity = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    remarks = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    class Meta:
        model = ExemptAssessment
        fields = ['id','exempt_assessment_roll','arpn','td_no','pin','lot_block_no','property_owner',
                  'address_of_property_owner','classification','assessed_value','legal_basis','effectivity',
                  'remarks',]
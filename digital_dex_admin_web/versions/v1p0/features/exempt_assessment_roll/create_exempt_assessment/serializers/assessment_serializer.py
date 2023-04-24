from rest_framework import serializers
from .......models.exempt_assessment_model import ExemptAssessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExemptAssessment
        fields = [
                  ############## ASSESSMENT ############
                  'id','exempt_assessment_roll','arpn','td_no','pin','lot_block_no','property_owner',
                  'address_of_property_owner','kind','classification','assessed_value','legal_basis','effectivity',
                  'remarks',
                  ]
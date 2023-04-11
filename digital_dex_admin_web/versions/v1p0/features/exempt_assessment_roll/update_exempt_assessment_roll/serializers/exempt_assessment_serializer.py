from rest_framework import serializers
from .......models.exempt_assessment_model import ExemptAssessment

class UpdateAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExemptAssessment
        fields = ['id','exempt_assessment_roll','arpn','td_no','pin','lot_block_no','property_owner',
                  'address_of_property_owner','kind','classification','assessed_value','prev_arpn','prev_td_no','effectivity',
                  'remarks',]
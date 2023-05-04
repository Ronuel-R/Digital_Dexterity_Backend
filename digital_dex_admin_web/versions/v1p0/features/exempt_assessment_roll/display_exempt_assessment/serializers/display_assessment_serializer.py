from rest_framework import serializers
from .......models.exempt_assessment_model import ExemptAssessment

class DisplayAssessmentSerializer(serializers.ModelSerializer):
    classification_display = serializers.CharField(source='get_classification_display')
    class Meta:
        model = ExemptAssessment
        fields = ['id','exempt_assessment_roll','arpn','td_no','pin','lot_block_no','property_owner',
                  'address_of_property_owner','kind','classification','classification_display','assessed_value','legal_basis','effectivity',
                  'remarks',
                  ]
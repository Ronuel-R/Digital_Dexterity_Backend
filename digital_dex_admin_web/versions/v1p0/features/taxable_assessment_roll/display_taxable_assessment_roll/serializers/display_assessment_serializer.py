from rest_framework import serializers
from .......models.taxable_assessment_model import TaxableAssessment

class DisplayAssessmentSerializer(serializers.ModelSerializer):
    classification_display= serializers.CharField(source='get_classification_display')
    class Meta:
        model = TaxableAssessment
        fields = ['id','tax_assessment_roll','arpn','td_no','pin','lot_block_no','property_owner',
                  'address_of_property_owner','kind','classification','classification_display','assessed_value','prev_arpn','prev_td_no','effectivity',
                  'remarks',
                  ]
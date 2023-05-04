from rest_framework import serializers
from .......models.tax_initial_assessment_model import InitialAssessment

class InitialAssessmentSerializer(serializers.ModelSerializer):
    classification_display = serializers.CharField(source='get_classification_display')
    class Meta:
        model = InitialAssessment
        fields = [
                  ############## INITIAL ASSESSMENT #########
                  'id','tax_form','classification','classification_display','area','market_value','actual_use','assessment_level',
                  'assessed_value',
                  ]
from rest_framework import serializers
from ......models.tax_initial_assessment_model import InitialAssessment

class InitialAssessmentSerializer(serializers.Serializer):

    class Meta:
        model = InitialAssessment
        fields = [
                  ############## INITIAL ASSESSMENT #########
                  'classification','area','market_value','actual_use','assessment_level',
                  'assessed_value',
                  
                  ]
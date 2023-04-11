from rest_framework import serializers
from ......models.exempt_assessment_roll_model import ExemptAssessmentRoll
from ..serializers.exempt_assessment_serializer import UpdateAssessmentSerializer

class UpdateExemptAssessmentRollSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExemptAssessmentRoll
        fields = ['prov_city', 'prov_city_index_no', 'mun_city', 'mun_city_index_no', 'barangay', 
                  'barangay_index_no', 'section_index_no','modified']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['assessments'] = UpdateAssessmentSerializer(instance.exemptassessment_set.all(),many=True).data
        return rep
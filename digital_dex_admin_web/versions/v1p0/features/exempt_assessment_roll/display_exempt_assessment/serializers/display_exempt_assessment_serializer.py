from rest_framework import serializers
from .......models.exempt_assessment_roll_model import ExemptAssessmentRoll
from ..serializers.display_assessment_serializer import DisplayAssessmentSerializer

class DisplayExemptAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExemptAssessmentRoll
        fields = ['id','revision_year','prov_city', 'prov_city_index_no', 'mun_city', 'mun_city_index_no', 'barangay',
                  'barangay_index_no', 'section','section_index_no','date_prepared','date_modified']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['assessments'] = DisplayAssessmentSerializer(instance.exemptassessment_set.all(),many=True).data
        rep['total_assessments'] = instance.exemptassessment_set.count()
        return rep
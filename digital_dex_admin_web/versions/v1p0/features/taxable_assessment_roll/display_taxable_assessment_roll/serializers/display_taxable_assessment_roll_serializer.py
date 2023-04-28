from rest_framework import serializers
from .......models.taxable_assessment_roll_model import TaxableAssessmentRoll
from .display_assessment_serializer import DisplayAssessmentSerializer

class DisplayTaxAssessmentRollSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxableAssessmentRoll
        fields = ['id','revision_year','prov_city', 'prov_city_index_no', 'mun_city', 'mun_city_index_no', 'barangay',
                  'barangay_index_no', 'section','section_index_no','date_prepared','date_modified']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['taxable_assessments'] = DisplayAssessmentSerializer(instance.taxableassessment_set.all(),many=True).data
        rep['total_assessments'] = instance.taxableassessment_set.count()
        return rep
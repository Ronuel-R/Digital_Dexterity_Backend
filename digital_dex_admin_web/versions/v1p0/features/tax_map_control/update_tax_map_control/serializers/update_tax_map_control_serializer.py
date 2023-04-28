from rest_framework import serializers
from .......models.tax_map_control_model import TaxMapControl
from ..serializers.assessment_serializer import UpdateAssessmentSerializer

class UpdateTaxMapControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxMapControl
        fields = ['id','prov_city', 'prov_city_index_no', 'mun_city', 'mun_city_index_no', 'barangay', 
                  'barangay_index_no', 'section_index_no']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['assessments'] = UpdateAssessmentSerializer(instance.assessment_set.all(),many=True).data
        return rep

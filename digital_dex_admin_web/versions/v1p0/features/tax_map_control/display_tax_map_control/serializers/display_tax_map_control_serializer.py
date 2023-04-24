from rest_framework import serializers
from .......models.tax_map_control_model import TaxMapControl
from ..serializers.assessment_serializer import DisplayAssessmentSerializer

class DisplayTaxMapControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxMapControl
        fields = ['prov_city', 'prov_city_index_no', 'mun_city', 'mun_city_index_no', 'barangay', 
                  'barangay_index_no', 'section_index_no',
                  ############ Static ######################
                  'date_modified'
                  ]
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['assessments'] = DisplayAssessmentSerializer(instance.assessment_set.all(),many=True).data
        rep['total_assessments'] = instance.assessment_set.count()
        return rep

from rest_framework import serializers
from .......models.taxable_assessment_roll_model import TaxableAssessmentRoll

class TaxAssessmentRollSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxableAssessmentRoll
        fields = ['prov_city', 'prov_city_index_no', 'mun_city', 'mun_city_index_no', 'barangay', 
                  'barangay_index_no', 'section_index_no','modified']
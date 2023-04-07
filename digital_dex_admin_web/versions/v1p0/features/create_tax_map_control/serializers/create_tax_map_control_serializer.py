from rest_framework import serializers
from ......models.tax_map_control_model import TaxMapControl

class CreateTaxMapControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxMapControl
        fields = ['prov_city', 'prov_city_index_no', 'mun_city', 'mun_city_index_no', 'barangay', 
                  'barangay_index_no', 'section_index_no']
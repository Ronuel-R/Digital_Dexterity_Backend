from rest_framework import serializers
from ......models.ownership_record_model import OwnsershipRecordCardModel
from ..serializers.display_records_serializer import DisplayRecordSerializer

class DisplayOwnershipRecordCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnsershipRecordCardModel
        fields = ['prov_city', 'prov_city_index_no', 'mun_city', 'mun_city_index_no', 'barangay', 
                  'barangay_index_no', 'section_index_no','modified']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['records'] = DisplayRecordSerializer(instance.recordcardmodel_set.all(),many=True).data
        return rep
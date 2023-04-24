from rest_framework import serializers
from .......models.ownership_record_model import OwnsershipRecordCardModel
from ..serializers.display_records_serializer import DisplayRecordSerializer

class DisplayOwnershipRecordCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnsershipRecordCardModel
        fields = ['id', 'name_of_owner', 'address', 'tel_no', 'tin', 
                  'date_prepared', 'prov_city_mun','index_no', 'modified']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['records'] = DisplayRecordSerializer(instance.recordcardmodel_set.all(),many=True).data
        rep['total_records'] = instance.recordcardmodel_set.count()
        return rep
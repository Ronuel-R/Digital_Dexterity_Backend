from rest_framework import serializers
from ......models.ownership_record_model import OwnsershipRecordCardModel
from ..serializers.update_records_serializer import UpdateRecordSerializer

class UpdateOwnershipRecordCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnsershipRecordCardModel
        fields = ['id', 'name_of_owner', 'address', 'tel_no', 'tin', 
                  'date_prepared', 'prov_city_mun','index_no', 'modified']
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['records'] = UpdateRecordSerializer(instance.recordcardmodel_set.all(),many=True).data
        return rep
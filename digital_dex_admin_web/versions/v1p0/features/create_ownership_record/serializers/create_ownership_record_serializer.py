from rest_framework import serializers
from ......models.ownership_record_model import OwnsershipRecordCardModel

class OwnershipRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnsershipRecordCardModel
        fields = ['id', 'name_of_owner', 'address', 'tel_no', 'tin', 
                  'date_prepared', 'prov_city_mun','index_no', 'modified']
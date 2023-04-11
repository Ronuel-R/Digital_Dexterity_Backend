from rest_framework import serializers
from ......models.record_model import RecordCardModel

class UpdateRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordCardModel
        fields = ['id','ownership','date_of_entry','kind','class_code','pin','title_no',
                  'lot_block_no','arp_no','td_no','previous_owner','location_of_property','area','market_value',
                  'assessed_value','remarks',
                  ]
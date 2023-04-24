from rest_framework import serializers
from .......models.ownership_record_model import OwnsershipRecordCardModel
from datetime import datetime
class OwnershipRecordSerializer(serializers.ModelSerializer):
    date_prepared = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d'])
    class Meta:
        model = OwnsershipRecordCardModel
        fields = ['id', 'name_of_owner', 'address', 'tel_no', 'tin', 
                  'date_prepared', 'prov_city_mun','index_no', 'modified']
def validate_dated(self, value):
    # Convert the date string to a date object
    date_obj = datetime.strptime(value, '%Y-%m-%d').date()
    # Format the date object as a string in the desired format
    date_str = date_obj.strftime('%Y-%m-%d')
    # Parse the formatted string as a date object
    formatted_date = datetime.strptime(date_str, '%m-%d-%Y').date()
    return formatted_date
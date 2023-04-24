from rest_framework import serializers
from .......models.taxable_assessment_roll_model import TaxableAssessmentRoll
from datetime import datetime

class TaxAssessmentRollSerializer(serializers.ModelSerializer):
    date_prepared = serializers.DateField(format="%Y-%m-%d", input_formats=['%Y-%m-%d'])
    class Meta:
        model = TaxableAssessmentRoll
        fields = ['revision_year','prov_city', 'prov_city_index_no', 'mun_city', 'mun_city_index_no', 'barangay',
                  'barangay_index_no', 'section','section_index_no','date_prepared','date_modified']

def validate_dated(self, value):
    # Convert the date string to a date object
    date_obj = datetime.strptime(value, '%Y-%m-%d').date()
    # Format the date object as a string in the desired format
    date_str = date_obj.strftime('%Y-%m-%d')
    # Parse the formatted string as a date object
    formatted_date = datetime.strptime(date_str, '%m-%d-%Y').date()
    return formatted_date
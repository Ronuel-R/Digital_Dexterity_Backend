from rest_framework import serializers
from .......models.assessment_model import Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    building_structure = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    machinery = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    others = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    remarks = serializers.CharField(required=False, allow_null=True,allow_blank=True)
    class Meta:
        model = Assessment
        fields = ['assessors_lot_no', 'survey_lot_no', 'land_title_no', 'land_area', 'land_class_code', 'name_of_owner',
                  'arp_no', 'td_no', 'building_structure', 'machinery', 'others','remarks']

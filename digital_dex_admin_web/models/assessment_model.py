from django.db import models
from .tax_map_control_model import TaxMapControl


class Assessment(models.Model):

    
    id = models.AutoField(primary_key=True)
    assessors_lot_no = models.IntegerField(null = True)
    survey_lot_no = models.CharField(max_length=255, null = True)
    land_title_no = models.CharField(max_length=255, null = True)
    land_area = models.IntegerField(null = True)
    land_class_code = models.CharField(max_length=255, null = True)
    name_of_owner = models.CharField(max_length=255, null = True)
    arp_no = models.CharField(max_length=255, null = True)
    td_no = models.CharField(max_length=255, null = True)
    building_structure = models.IntegerField(null = True)
    machinery = models.IntegerField(null = True)
    others = models.CharField(max_length=255, null = True)
    remarks = models.CharField(max_length=255, null = True)
    tax_map_control = models.ForeignKey(TaxMapControl, on_delete=models.CASCADE, null=True)

    class Meta:
            verbose_name = 'Assessment'
            verbose_name_plural = 'Assessments'

    def __str__(self):
        return str(self.id)
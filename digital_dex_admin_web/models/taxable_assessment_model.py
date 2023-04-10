from django.db import models
from .taxable_assessment_roll_model import TaxableAssessmentRoll


class TaxableAssessment(models.Model):

    id = models.AutoField(primary_key=True)
    tax_assessment_roll = models.ForeignKey(TaxableAssessmentRoll, on_delete=models.CASCADE, null=True)
    arpn = models.CharField(max_length=255, null = True)
    td_no = models.CharField(max_length=255, null = True)
    pin = models.IntegerField(null = True)
    lot_block_no = models.CharField(max_length=255, null = True)
    property_owner = models.CharField(max_length=255, null = True)
    address_of_property_owner = models.CharField(max_length=255, null = True)
    kind = models.CharField(max_length=255, null = True)
    classification = models.CharField(max_length=255, null = True)
    assessed_value = models.IntegerField(null = True)
    prev_arpn = models.CharField(max_length=255, null = True)
    prev_td_no = models.CharField(max_length=255, null = True)
    effectivity = models.CharField(max_length=255, null = True)
    remarks = models.CharField(max_length=255, null = True)
    

    class Meta:
            verbose_name = 'Taxable Assessment'
            verbose_name_plural = 'Taxable Assessments'

    def __str__(self):
        return str(self.id)
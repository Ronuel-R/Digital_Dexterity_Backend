from django.db import models
from .exempt_assessment_roll_model import ExemptAssessmentRoll


class ExemptAssessment(models.Model):

    id = models.AutoField(primary_key=True)
    exempt_assessment_roll = models.ForeignKey(ExemptAssessmentRoll, on_delete=models.CASCADE, null=True)
    arpn = models.CharField(max_length=255, null = True)
    td_no = models.CharField(max_length=255, null = True)
    pin = models.IntegerField(null = True)
    lot_block_no = models.CharField(max_length=255, null = True)
    property_owner = models.CharField(max_length=255, null = True)
    address_of_property_owner = models.CharField(max_length=255, null = True)
    kind = models.CharField(max_length=255, null = True)
    CLASSIFICATION_CHOICES = (
        ('R', 'Residential'),
        ('A', 'Agricultural'),
        ('C', 'Commercial'),
        ('I', 'Industrial'),
        ('S', 'Special'),
        ('T', 'Timberland'),
        ('M', 'Mineral'),
    )
    classification = models.CharField(max_length=1, choices=CLASSIFICATION_CHOICES, null = True)
    assessed_value = models.FloatField(null = True)
    legal_basis = models.CharField(max_length=255, null = True)
    effectivity = models.CharField(max_length=255, null = True)
    remarks = models.CharField(max_length=255, null = True)


    class Meta:
            verbose_name = 'Exempt Assessment'
            verbose_name_plural = 'Exempt Assessments'

    def __str__(self):
        return str(self.id)
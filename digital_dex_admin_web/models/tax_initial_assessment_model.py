from django.db import models
from .tax_form_model import TaxForm

class InitialAssessment(models.Model):
    id = models.AutoField(primary_key=True)
    tax_form = models.ForeignKey(TaxForm , on_delete= models.CASCADE, null=True)
    classification = models.CharField(max_length=255,null=True)
    area = models.FloatField(null=True)
    market_value = models.FloatField(null=True)
    actual_use = models.CharField(max_length=255,null=True)
    assessment_level = models.FloatField(null=True)
    assessed_value = models.FloatField(null=True)
    

    class Meta:
        verbose_name = 'Initial Assessment'
        verbose_name_plural = 'Initial Assessment'

    def __str__(self):
        return str(self.id)

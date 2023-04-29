from django.db import models
from .tax_form_model import TaxForm

class InitialAssessment(models.Model):
    id = models.AutoField(primary_key=True)
    tax_form = models.ForeignKey(TaxForm , on_delete= models.CASCADE, null=True)
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
    area = models.FloatField(default=0.0)
    market_value = models.FloatField(default=0.0)
    actual_use = models.CharField(max_length=255,null=True)
    assessment_level = models.FloatField(default=0.0)
    assessed_value = models.FloatField(default=0.0)


    class Meta:
        verbose_name = 'Tax Declaration of Real Property Initial Assessment'
        verbose_name_plural = 'Tax Declaration of Real Property Tax Initial Assessments'

    def __str__(self):
        return str(self.id)

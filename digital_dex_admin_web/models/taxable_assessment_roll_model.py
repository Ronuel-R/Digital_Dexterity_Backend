from django.db import models

class TaxableAssessmentRoll(models.Model):

    id = models.AutoField(primary_key=True)
    revision_year = models.IntegerField(null=True)
    prov_city = models.CharField(max_length=255, null=True)
    prov_city_index_no = models.IntegerField(null=True)
    mun_city = models.CharField(max_length=255, null=True)
    mun_city_index_no = models.IntegerField(null=True)
    barangay = models.CharField(max_length=255, null=True)
    barangay_index_no = models.IntegerField(null=True)
    section = models.IntegerField(null=True)
    section_index_no = models.IntegerField(null=True)
    date_prepared = models.DateField(null = True)
    date_modified = models.DateField(null=True)

    class Meta:
        verbose_name = 'Taxable Assessment Roll'
        verbose_name_plural = 'Taxable Assessment Rolls'

    def __str__(self):
        return str(self.id)
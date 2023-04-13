from django.db import models

class TaxMapControl(models.Model):

    id = models.AutoField(primary_key=True)

    prov_city = models.CharField(max_length=255, null=True)
    prov_city_index_no = models.IntegerField(null=True)
    mun_city = models.CharField(max_length=255, null=True)
    mun_city_index_no = models.IntegerField(null=True)
    barangay = models.CharField(max_length=255, null=True)
    barangay_index_no = models.IntegerField(null=True)
    section_index_no = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Tax Map Control'
        verbose_name_plural = 'Tax Map Control'

    def __str__(self):
        return str(self.id)
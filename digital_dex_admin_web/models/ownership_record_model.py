from django.db import models

class OwnsershipRecordCardModel(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_owner = models.CharField(max_length=255, null = True)
    address = models.CharField(max_length=255, null = True)
    tel_no = models.CharField(max_length=255, null = True)
    tin = models.CharField(max_length=255, null = True)
    date_prepared = models.DateField(null = True)
    prov_city_mun = models.CharField(max_length=255, null = True)
    index_no = models.IntegerField(null = True)
    modified = models.DateField(null = True)

    class Meta:
        verbose_name = 'Ownership Record'
        verbose_name_plural = 'Ownership Records'

    def __str__(self):
        return str(self.id)
from django.db import models
from .ownership_record_model import OwnsershipRecordCardModel

class RecordCardModel(models.Model):

    id = models.AutoField(primary_key=True)
    ownership = models.ForeignKey(OwnsershipRecordCardModel, on_delete=models.CASCADE, null=True)
    date_of_entry = models.CharField(max_length=255, null = True)
    kind = models.CharField(max_length=255, null = True)
    class_code = models.CharField(max_length=255, null = True)
    pin = models.IntegerField(null = True)
    title_no = models.CharField(max_length=255,null = True)
    lot_block_no = models.CharField(max_length=255, null = True)
    arp_no = models.CharField(max_length=255, null = True)
    td_no = models.CharField(max_length=255, null = True)
    previous_owner = models.CharField(max_length=255, null = True)
    location_of_property = models.CharField(max_length=255, null = True)
    area = models.FloatField(null = True)
    market_value = models.FloatField(null = True)
    assessed_value = models.FloatField(null = True)
    remarks = models.CharField(max_length=255, null = True)

    class Meta:
        verbose_name = 'Ownership Record'
        verbose_name_plural = 'Ownership Records'

    def __str__(self):
        return str(self.id)
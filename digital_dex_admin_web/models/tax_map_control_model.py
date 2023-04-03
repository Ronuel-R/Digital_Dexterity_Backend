from django.db import models

class TaxMapControl(models.Model):

    id = models.AutoField(primary_key=True)

    prov_city = models.CharField(max_length=255, null = True)
    prov_city_index_no = models.IntegerField(null = True)
    mun_city = models.CharField(max_length=255, null = True)
    mun_city_index_no = models. IntegerField(null = True)
    barangay = models.CharField(max_length=255, null = True)
    barangay_index_no = models.IntegerField(null = True)
    section_index_no = models.IntegerField(null = True)

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

    class Meta:
            verbose_name = 'Tax Map Control'
            verbose_name_plural = 'Tax Map Control'

    def __str__(self):
        return str(self.prov_city)
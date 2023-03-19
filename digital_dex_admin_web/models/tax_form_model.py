from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .admin_model import Admin

def upload_signature_approval_location(instance, filename):
    
    new_file = filename
    return 'Approved By/%s' % (new_file)

class TaxForm(models.Model):
    td_no = models.IntegerField()
    property_identification_no = models.IntegerField()

############## OWNER ########################
    owner = models.CharField(max_length=255)
    owner_tin = models.IntegerField()
    owner_address = models.CharField(max_length=255)
    owner_tel_no = models.CharField(max_length=255)

############## Admin ####################
    administrator_beneficial_user = models.CharField(max_length=255)
    admin_tin = models.IntegerField()
    admin_tel_no = models.CharField(max_length=255)

############## PROPERTY ##################
    property_location = models.CharField(max_length=255)
    oct_no = models.IntegerField()
    survey_no = models.IntegerField()
    cct = models.CharField(max_length=255)
    lot_no = models.IntegerField()
    dated = models.DateField(max_length=255)
    blk_no = models.IntegerField()

############## BOUNDARY ###################
    north = models.FloatField(max_length=255)
    west = models.FloatField(max_length=255)
    east = models.FloatField(max_length=255)
    south = models.FloatField(max_length=255)

############## KIND OF PROPERT ############
    PROPERTY_CHOICES = (
        ('L', 'Land'),
        ('B', 'Building'),
        ('M', 'Machinery'),
        ('O', 'Others'),
    )
    property_choices = models.CharField(max_length=1, choices=PROPERTY_CHOICES, null = True)
    no_of_storeys = models.IntegerField()
    brief_description = models.CharField(max_length=255)

############## INITIAL ASSESSMENT #########
    classification = models.CharField(max_length=255)
    area = models.FloatField(max_length=255)
    market_value = models.FloatField(max_length=255)
    actual_use = models.CharField(max_length=255)
    assessment_level = models.FloatField(max_length=255)
    assessment_value = models.FloatField(max_length=255)
    total_assessed_value = models.CharField(max_length=255)

############# FINAL ASSESSMENT ############
    TAXABLE_CHOICES = (
        ('T', 'Taxable'),
        ('E', 'Exempt'),
    )
    taxable = models.CharField(max_length=1, choices=TAXABLE_CHOICES, null = True)

############# EFFECTIVITY OF ASSESSMENT ############

    # qtr = di ko alam to
    year = models.DateField(max_length=255)
    approved_by = models.ImageField(blank = True, upload_to=upload_signature_approval_location,null = True)
    date_assessed = models.DateTimeField(null=False,editable=False)

############# CANCEL OWNERSHIP #####################

    cancels_td_no = models.IntegerField()
    cancel_owner = models.CharField(max_length=255)
    cancel_previous_av_pph = models.CharField(max_length=255)
    memoranda = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Tax Declaration of Real Property'

    def __str__(self):
        return str(self.td_no)

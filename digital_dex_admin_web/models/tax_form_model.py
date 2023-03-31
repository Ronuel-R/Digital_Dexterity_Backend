from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .tax_initial_assessment_model import InitialAssessment

def upload_signature_approval_location(instance, filename):
    
    new_file = filename
    return 'Approved By/%s' % (new_file)

class TaxForm(models.Model):
    td_no = models.IntegerField(null=True)
    property_identification_no = models.IntegerField(null=True)

############## OWNER ########################
    owner = models.CharField(max_length=255,null=True)
    owner_tin = models.IntegerField(null=True)
    owner_address = models.CharField(max_length=255,null=True)
    owner_tel_no = models.CharField(max_length=255,null=True)

############## Admin ####################
    administrator_beneficial_user = models.CharField(max_length=255,null=True)
    admin_tin = models.IntegerField(null=True)
    admin_address = models.CharField(max_length=255,null=True)
    admin_tel_no = models.CharField(max_length=255,null=True)

############## PROPERTY ##################
    property_location = models.CharField(max_length=255,null=True)
    oct_no = models.IntegerField(null=True)
    survey_no = models.IntegerField(null=True)
    cct = models.CharField(max_length=255,null=True)
    lot_no = models.IntegerField(null=True)
    dated = models.DateField(max_length=255,null=True)
    blk_no = models.IntegerField(null=True)

############## BOUNDARY ###################
    north = models.FloatField(max_length=255,null=True)
    west = models.FloatField(max_length=255,null=True)
    east = models.FloatField(max_length=255,null=True)
    south = models.FloatField(max_length=255,null=True)

############## KIND OF PROPERT ############
    PROPERTY_CHOICES = (
        ('L', 'Land'),
        ('B', 'Building'),
        ('M', 'Machinery'),
        ('O', 'Others'),
    )
    property_choices = models.CharField(max_length=1, choices=PROPERTY_CHOICES, null = True)

    mach_brief_description = models.TextField(max_length=255,null=True)

    no_of_storeys = models.IntegerField(null=True)
    brief_description = models.TextField(max_length=255,null=True)

    specify= models.TextField(max_length=255,null=True)

############## INITIAL ASSESSMENT #########

    initial_assessment = models.ManyToManyField(InitialAssessment, blank=True, null=True)

    total_assessed_value_words = models.CharField(max_length=255,null=True)
    total_assessed_value = models.FloatField(null=True)
    total_market_value = models.FloatField(null=True)

############# FINAL ASSESSMENT ############
    TAXABLE_CHOICES = (
        ('T', 'Taxable'),
        ('E', 'Exempt'),
    )
    taxable = models.CharField(max_length=1, choices=TAXABLE_CHOICES, null = True)

############# EFFECTIVITY OF ASSESSMENT ############

    qtr = models.IntegerField(null=True)
    year = models.DateField(max_length=255,null=True)
    approved_by = models.ImageField(blank = True, upload_to=upload_signature_approval_location,null = True)
    date_assessed = models.DateField(null=False)

############# CANCEL OWNERSHIP #####################

    cancels_td_no = models.IntegerField(null=True)
    cancel_owner = models.CharField(max_length=255,null=True)
    cancel_previous_av_pph = models.CharField(max_length=255,null=True)
    memoranda = models.TextField(max_length=255,null=True)

    class Meta:
        verbose_name = 'Tax Declaration of Real Property'
        verbose_name_plural = 'Tax Declaration of Real Properties'

    def __str__(self):
        return str(self.td_no)

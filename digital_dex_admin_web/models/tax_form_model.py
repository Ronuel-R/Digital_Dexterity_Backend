from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def upload_signature_approval_location(instance, filename):

    new_file = filename
    return 'Approved By/%s' % (new_file)

class TaxForm(models.Model):
    id = models.AutoField(primary_key=True)
    td_no = models.CharField(null=True,max_length=255)
    property_identification_no = models.IntegerField(null=True)

############## OWNER ########################
    owner = models.CharField(max_length=255,null=True)
    owner_tin = models.IntegerField(null=True)
    owner_address = models.CharField(max_length=255,null=True)
    owner_tel_no = models.CharField(max_length=255,null=True)

############## Admin ####################
    administrator_beneficial_user = models.CharField(max_length=255,null=True)
    admin_tin = models.CharField(max_length=255,null=True)
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
    north = models.CharField(max_length=255,null=True)
    west = models.CharField(max_length=255,null=True)
    east = models.CharField(max_length=255,null=True)
    south = models.CharField(max_length=255,null=True)

############## KIND OF PROPERT ############
    PROPERTY_CHOICES = (
        ('L', 'Land'),
        ('B', 'Building'),
        ('M', 'Machinery'),
        ('O', 'Others'),
    )
    property_choices = models.CharField(max_length=1, choices=PROPERTY_CHOICES, null = True)
    mach_brief_description = models.TextField(max_length=255,null=True,blank=True)
    no_of_storeys = models.TextField(max_length=255,null=True,blank=True)
    brief_description = models.TextField(max_length=255,null=True,blank=True)
    specify= models.TextField(max_length=255,null=True,blank=True)

############## INITIAL ASSESSMENT #########

    total_assessed_value_words = models.CharField(max_length=255,null=True)
    # total_assessed_value = models.FloatField(null=True)
    # total_market_value = models.FloatField(null=True)

############# FINAL ASSESSMENT ############
    TAXABLE_CHOICES = (
        ('T', 'Taxable'),
        ('E', 'Exempt'),
    )
    tax_status = models.CharField(max_length=1, choices=TAXABLE_CHOICES, null = True)

############# EFFECTIVITY OF ASSESSMENT ############

    qtr = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    approved_by = models.CharField(null=True,max_length=255)
    date_assessed = models.DateField(null=False)

############# CANCEL OWNERSHIP #####################

    cancels_td_no = models.CharField(null=True,max_length=255)
    cancel_owner = models.CharField(max_length=255,null=True)
    cancel_previous_av_php = models.IntegerField(null=True)
    memoranda = models.TextField(max_length=255,null=True)

################# Notes #######################

    sanggunian = models.CharField(max_length=255,null=True)
    under_ord_num = models.IntegerField(null=True)
    notes_date = models.DateField(null=True)

############# Date Modified ########################
    STATUS_CHOICES = (
        ('R', 'Recently Updated'),
        ('P', 'Processing'),
    )
    date_modified = models.DateField(null = True)
    created = models.DateField(default=timezone.now, null=False,editable=False)
    status_choices = models.CharField(max_length=1, choices=STATUS_CHOICES, null = True)

    class Meta:
        verbose_name = 'Tax Declaration of Real Property'
        verbose_name_plural = 'Tax Declaration of Real Properties'

    def __str__(self):
        return str(self.id)

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def upload_profile_location(instance, filename):
    
    new_file = filename
    return 'Profiles/%s' % (new_file)

def upload_signature_location(instance, filename):
    
    new_file = filename
    return 'Signature/%s' % (new_file)

class Admin(models.Model):
    user = models.OneToOneField(User, null = True ,on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank = True, upload_to=upload_profile_location,null = True)
    full_name = models.CharField(max_length=255, null = True)
    age = models.IntegerField(null = True)
    birthday = models.DateField(null = True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null = True)
    phone_num = models.CharField(max_length=11, null = True)
    position = models.CharField(max_length=255,null = True)
    date_created = models.DateTimeField(default=timezone.now, null=False,editable=False)

    class Meta:
        verbose_name = 'Admin account'
        verbose_name_plural = 'Admin account'

    def __str__(self):
        return str(self.full_name)

from django.contrib import admin
from .models.admin_model import Admin
from .models.tax_form_model import TaxForm


admin.site.register(Admin)
admin.site.register(TaxForm)

from django.contrib import admin
from .models.admin_model import Admin
from .models.tax_map_control_model import TaxMapControl
from .models.assessment_model import Assessment

admin.site.register(Admin)
admin.site.register(TaxMapControl)
admin.site.register(Assessment)

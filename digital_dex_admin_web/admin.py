from django.contrib import admin
from .models.admin_model import Admin
from .models.tax_form_model import TaxForm
from .models.tax_initial_assessment_model import InitialAssessment


admin.site.register(Admin)
admin.site.register(TaxForm)
admin.site.register(InitialAssessment)



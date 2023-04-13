from django.contrib import admin
from .models.admin_model import Admin
from .models.tax_form_model import TaxForm
from .models.tax_initial_assessment_model import InitialAssessment
from .models.tax_map_control_model import TaxMapControl
from .models.assessment_model import Assessment


admin.site.register(Admin)
admin.site.register(TaxForm)
admin.site.register(InitialAssessment)
admin.site.register(TaxMapControl)
admin.site.register(Assessment)

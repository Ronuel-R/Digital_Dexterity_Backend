from django.contrib import admin
from .models.admin_model import Admin
from .models.taxable_assessment_model import TaxableAssessment
from .models.taxable_assessment_roll_model import TaxableAssessmentRoll

admin.site.register(Admin)
admin.site.register(TaxableAssessment)
admin.site.register(TaxableAssessmentRoll)
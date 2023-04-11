from django.contrib import admin
from .models.admin_model import Admin
from .models.exempt_assessment_model import ExemptAssessment
from .models.exempt_assessment_roll_model import ExemptAssessmentRoll

admin.site.register(Admin)
admin.site.register(ExemptAssessment)
admin.site.register(ExemptAssessmentRoll)
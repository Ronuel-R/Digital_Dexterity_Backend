from django.contrib import admin
from .models.admin_model import Admin
from .models.tax_form_model import TaxForm
from .models.tax_initial_assessment_model import InitialAssessment
from .models.tax_map_control_model import TaxMapControl
from .models.assessment_model import Assessment
from .models.taxable_assessment_model import TaxableAssessment
from .models.taxable_assessment_roll_model import TaxableAssessmentRoll
from .models.exempt_assessment_model import ExemptAssessment
from .models.exempt_assessment_roll_model import ExemptAssessmentRoll
from .models.ownership_record_model import OwnsershipRecordCardModel
from .models.record_model import RecordCardModel


admin.site.register(Admin)
admin.site.register(TaxForm)
admin.site.register(InitialAssessment)
admin.site.register(TaxMapControl)
admin.site.register(Assessment)
admin.site.register(TaxableAssessment)
admin.site.register(TaxableAssessmentRoll)
admin.site.register(ExemptAssessment)
admin.site.register(ExemptAssessmentRoll)
admin.site.register(OwnsershipRecordCardModel)
admin.site.register(RecordCardModel)

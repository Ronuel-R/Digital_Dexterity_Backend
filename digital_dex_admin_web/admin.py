from django.contrib import admin
from .models.admin_model import Admin
from .models.ownership_record_model import OwnsershipRecordCardModel
from .models.record_model import RecordCardModel

admin.site.register(Admin)
admin.site.register(OwnsershipRecordCardModel)
admin.site.register(RecordCardModel)

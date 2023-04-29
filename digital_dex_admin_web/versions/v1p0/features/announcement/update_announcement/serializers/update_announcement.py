from rest_framework import serializers
from .......models.announcement_model import Announcement

class UpdateAnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcement
        fields = ['id','message']
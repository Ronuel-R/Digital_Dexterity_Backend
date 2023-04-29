from django.db import models

class Announcement(models.Model):
    message= models.TextField(max_length=500, null=True)

    def __str__(self):
        return str(self.id)
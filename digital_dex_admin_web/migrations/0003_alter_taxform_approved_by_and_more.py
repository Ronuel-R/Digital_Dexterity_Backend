# Generated by Django 4.1.7 on 2023-03-05 11:11

import digital_dex_admin_web.models.tax_form_model
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital_dex_admin_web', '0002_alter_taxform_approved_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxform',
            name='approved_by',
            field=models.ImageField(blank=True, null=True, upload_to=digital_dex_admin_web.models.tax_form_model.upload_signature_approval_location),
        ),
        migrations.AlterField(
            model_name='taxform',
            name='date_assessed',
            field=models.DateTimeField(editable=False),
        ),
    ]

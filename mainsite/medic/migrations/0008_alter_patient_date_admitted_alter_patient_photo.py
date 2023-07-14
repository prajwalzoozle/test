# Generated by Django 4.2.3 on 2023-07-12 12:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0007_alter_patient_date_admitted_alter_patient_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_admitted',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 12, 20, 27, 74495, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='photo',
            field=models.FileField(default=None, null=True, upload_to='patient/<built-in function id>/'),
        ),
    ]

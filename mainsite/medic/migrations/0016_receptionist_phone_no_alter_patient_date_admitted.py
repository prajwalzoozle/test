# Generated by Django 4.2.3 on 2023-07-13 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0015_receptionist_doctor_password_doctor_phone_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receptionist',
            name='phone_no',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_admitted',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 6, 45, 50, 196661, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-12 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0011_alter_patient_date_admitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_admitted',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 12, 27, 51, 624138, tzinfo=datetime.timezone.utc)),
        ),
    ]

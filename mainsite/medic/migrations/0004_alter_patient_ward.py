# Generated by Django 4.2.3 on 2023-07-10 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0003_patient_treats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ward',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='medic.ward'),
        ),
    ]

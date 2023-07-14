# Generated by Django 4.2.3 on 2023-07-07 06:12

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(choices=[(django.utils.timezone.now, 'today'), (datetime.datetime(2023, 7, 8, 6, 12, 43, 830250, tzinfo=datetime.timezone.utc), 'tomarrow')], verbose_name='date published'),
        ),
    ]

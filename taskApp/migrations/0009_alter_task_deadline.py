# Generated by Django 5.1.3 on 2025-01-01 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0008_delete_search'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
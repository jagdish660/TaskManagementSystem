# Generated by Django 5.1.4 on 2024-12-31 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0003_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-31 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskApp', '0002_alter_task_deadline_alter_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]

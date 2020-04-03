# Generated by Django 2.0.7 on 2020-03-31 12:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hiringapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='activity_uuid',
            field=models.UUIDField(default=uuid.UUID('71ab8c24-66aa-4298-8d1e-eb3f66304ec1'), primary_key=True, serialize=False),
        ),
    ]
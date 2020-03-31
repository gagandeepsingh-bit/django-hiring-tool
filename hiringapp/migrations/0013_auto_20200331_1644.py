# Generated by Django 2.0.7 on 2020-03-31 11:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hiringapp', '0012_auto_20200330_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='activity_uuid_link',
        ),
        migrations.AddField(
            model_name='submission',
            name='activity_uuid',
            field=models.UUIDField(default=uuid.UUID('d5b54241-ad34-4368-85b2-eba296eb4f7f'), primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 2.0.7 on 2020-03-31 11:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hiringapp', '0021_auto_20200331_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='activity_uuid_link',
        ),
        migrations.AddField(
            model_name='submission',
            name='activity_uuid',
            field=models.UUIDField(default=uuid.UUID('a8dfbd3d-2b42-415a-a457-f2dc53464726'), primary_key=True, serialize=False),
        ),
    ]

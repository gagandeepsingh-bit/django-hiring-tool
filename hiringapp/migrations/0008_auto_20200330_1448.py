# Generated by Django 2.0.7 on 2020-03-30 09:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hiringapp', '0007_auto_20200330_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='activity_invite_link',
        ),
        migrations.AddField(
            model_name='submission',
            name='activity_uuid_link',
            field=models.UUIDField(default=uuid.UUID('79274d93-a07e-43a6-8273-7bb70f14a1ea'), primary_key=True, serialize=False),
        ),
    ]
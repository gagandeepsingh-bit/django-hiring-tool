# Generated by Django 2.0.7 on 2020-03-30 09:43

from django.db import migrations, models
import hiringapp.utils
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hiringapp', '0009_auto_20200330_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailmodel',
            name='mail_status',
        ),
        migrations.AddField(
            model_name='mailmodel',
            name='mail_type',
            field=models.CharField(choices=[(hiringapp.utils.EmailType('invitation'), 'invitation'), (hiringapp.utils.EmailType('reminder'), 'reminder'), (hiringapp.utils.EmailType('feedback'), 'feedback')], default=hiringapp.utils.EmailType('invitation'), max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='activity_uuid_link',
            field=models.UUIDField(default=uuid.UUID('dc999d85-4cc4-4db6-ac7a-9a5ec59e5618'), primary_key=True, serialize=False),
        ),
    ]
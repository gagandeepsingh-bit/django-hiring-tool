# Generated by Django 2.0.7 on 2020-04-24 08:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("activitylauncher", "0003_auto_20200424_1228"),
    ]

    operations = [
        migrations.RenameModel(old_name="Submission", new_name="Invitation",),
    ]
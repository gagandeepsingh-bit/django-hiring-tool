# Generated by Django 2.0.7 on 2020-03-30 09:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hiringapp', '0008_auto_20200330_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='activity_uuid_link',
            field=models.UUIDField(default=uuid.UUID('3dd91eec-e264-4475-8249-e509d44ecadd'), primary_key=True, serialize=False),
        ),
    ]
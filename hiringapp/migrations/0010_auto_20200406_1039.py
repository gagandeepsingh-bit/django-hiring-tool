# Generated by Django 2.0.7 on 2020-04-06 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiringapp', '0009_auto_20200406_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='activity_solution_link',
            field=models.URLField(blank=True, editable=False, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='activity_start_time',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
# Generated by Django 2.0.7 on 2020-04-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailingapp', '0002_mailsummary_mail_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailsummary',
            name='mail_status',
            field=models.CharField(choices=[('SENT', 'Sent'), ('NOTSENT', 'NotSent')], default='NOTSENT', max_length=7),
        ),
    ]

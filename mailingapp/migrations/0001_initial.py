# Generated by Django 2.0.7 on 2020-04-14 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mailingapp.constants
import oauth2client.contrib.django_util.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_type', models.CharField(choices=[('invitation', 'INVITATION'), ('reminder_to_start', 'START_REMINDER'), ('activity_expired', 'ACTIVITY_EXPIRED'), ('activity_solution', 'ACTIVITY_SOLUTION'), ('reminder_to_submit', 'SUBMISSION_REMINDER')], default=mailingapp.constants.EmailType('invitation'), max_length=100, unique=True)),
                ('mail_subject', models.CharField(max_length=100)),
                ('mail_content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='GmailCredential',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('credential', oauth2client.contrib.django_util.models.CredentialsField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MailSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_type', models.CharField(choices=[('invitation', 'INVITATION'), ('reminder_to_start', 'START_REMINDER'), ('activity_expired', 'ACTIVITY_EXPIRED'), ('activity_solution', 'ACTIVITY_SOLUTION'), ('reminder_to_submit', 'SUBMISSION_REMINDER')], default=mailingapp.constants.EmailType('invitation'), max_length=100)),
                ('activity_uuid', models.UUIDField(null=True)),
                ('candidate_name', models.CharField(max_length=200)),
                ('date_of_mail', models.DateTimeField(blank=True, null=True)),
                ('mail_status', models.CharField(choices=[('SENT', 'sent'), ('NOTSENT', 'not_sent')], default='NOTSENT', max_length=7)),
            ],
        ),
    ]

import httplib2
from googleapiclient.discovery import build
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from . import models
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_util.storage import DjangoORMStorage
from django.shortcuts import render,redirect
from httplib2 import Http
from apiclient import errors
from email.mime.text import MIMEText
import base64
from oauth2client import service_account
from django.contrib import messages
from django.views.generic.edit import FormView
from mysite import settings
from .utils import FLOW

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)    


def get_mail_service(user):
    storage = DjangoORMStorage(models.CredentialsModel, 'id', user, 'credential')
    credential = storage.get()
    if credential is None or credential.invalid:
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)
    service = build('gmail', 'v1', credentials=credential,cache_discovery=False)
    return service

def create_messages(submission,email_type):
    #logic to create message from submission details and email_type 
    mail=models.MailModel.objects.get(mail_type=email_type)
    message=mail.mail_content
    mail_body=create_mail_body(submission,email_type,message)
    message=MIMEText(mail_body,'html')
    message['to']=submission.candidate_email
    message['subject']=mail.mail_subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def create_mail_body(submission,email_type,message):
    mail_body=""
    if email_type=='reminder':
        mail_body=message.format(candidate_name=submission.candidate_name,activity_duration=submission.activity_duration,activity_uuid=submission.activity_uuid)
    elif email_type=='invitation':
        mail_body=message.format(candidate_name=submission.candidate_name,activity_duration=submission.activity_duration,activity_uuid=submission.activity_uuid)

    return mail_body

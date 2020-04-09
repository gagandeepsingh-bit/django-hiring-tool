from django.test import TestCase, Client
from hiringapp.views import*
import uuid
from hiringapp.models import Submission
from unittest.mock import patch
from django.contrib.auth.models import User
from hiringapp.utils import ActivityStatus


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.submission_invite_url_with_random_uuid = reverse(
            'submission_invite', args=(uuid.uuid4(),))
        self.submission_solution_url_with_random_uuid = reverse(
            'submission_solution', args=(uuid.uuid4(),))
        self.gmail_authenticate_url=reverse('gmail_authenticate')

    def test_submission_invite_GET(self):
        response = self.client.get(self.submission_invite_url_with_random_uuid)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hiringapp/display_activity.html')

    @patch('hiringapp.tasks.send_emails.delay')
    def test_submission_invite_with_radom_uuid_POST(self, mocked_send_emails):
        response = self.client.post(
            self.submission_invite_url_with_random_uuid)
        self.assertEquals(response.status_code, 404)

    @patch('hiringapp.tasks.send_emails.delay')
    def test_submission_invite_with_valid_uuid_POST(self, mocked_send_emails):
        submission = Submission.objects.create()
        submission_invite_url_with_valid_uuid = reverse(
            'submission_invite', args=(submission.activity_uuid,))
        response = self.client.post(submission_invite_url_with_valid_uuid)
        self.assertEquals(response.status_code, 302)
        submission = Submission.objects.get(
            activity_uuid=submission.activity_uuid)
        self.assertEquals(submission.activity_status, ActivityStatus.Started.value)

    def test_submission_solution_with_random_uuid_POST(self):
        response = self.client.post(
            self.submission_solution_url_with_random_uuid)
        self.assertEquals(response.status_code, 404)

    @patch('hiringapp.tasks.send_emails.delay')
    def test_submission_solution_with_valid_uuid_POST(self, mocked_send_emails):
        submission = Submission.objects.create()
        submission_solution_url_with_valid_uuid = reverse(
            'submission_solution', args=(submission.activity_uuid,))
        response = self.client.post(submission_solution_url_with_valid_uuid, {
                                    'solution_link': 'link'})
        self.assertEquals(response.status_code, 302)
        submission = Submission.objects.get(
            activity_uuid=submission.activity_uuid)
        self.assertEquals(submission.activity_status, ActivityStatus.Submitted.value)
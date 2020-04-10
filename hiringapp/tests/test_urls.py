from django.test import TestCase
from django.urls import reverse, resolve
import uuid
from hiringapp.views import*


class TestUrls(TestCase):
    def test_submission_invite_url_resolved(self):
        url = reverse('submission_invite', args=(uuid.uuid4(),))
        self.assertEqual(resolve(url).func.view_class, SubmissionInviteView)

    def test_submission_solution_url_resolved(self):
        url = reverse('submission_solution', args=(uuid.uuid4(),))
        self.assertEqual(resolve(url).func.view_class, SubmitSolutionView)

import pytest
from django.test import TestCase
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

'''
Testing Authentication models creation
'''

class TestUser(TestCase):
    def setUp(self):
        self.user = mixer.blend('authentication.User')

    def test_model_creation(self):
        self.assertEqual(self.user.pk, 1)

    
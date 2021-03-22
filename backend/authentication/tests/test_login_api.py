from rest_framework.test import APITestCase
from django.test import RequestFactory
from authentication.models import User
from django.urls import resolve, reverse
from rest_framework import status

from authentication.views import LoginAPIView


class TestSetUp(APITestCase):
    def setUp(self):
        self.url = reverse('authentication:login')
        self.login_view = resolve(self.url)
        self.user = User.objects.create({
            'username': 'testuser',
            'email': "test@user.io",
            'password': 'test@user',
            'phone_number': '231895049034',
            'firstname': 'namefirst',
            'lastname': 'namelast'
        })

        self.valid_username = {
            'username': 'testuser',
            'password': 'test@user',
        }
        self.invalid_password = {
            'username': 'testuser',
            'password': 'test@user2',
        }
        self.valid_email = {
            'email': "test@user.io",
            'password': 'test@user',
        }
        self.invalid_username = {
            'username': 'test.user',
            'password': 'test@user',
        }
        self.invalid_email = {
            'email': 'test.u@ser.io',
            'password': 'test@user',
        }
        self.empty_fields = {
            'username': '',
            'password': 'test@user',
        }


class TestLoginAPI(TestSetUp):
    def test_valid_login_username(self):
        '''Login succeeds'''

        resp = self.client.post(
            self.url,
            self.valid_username
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn('token', resp.data)

    def test_valid_login_email(self):
        '''Login succeeds'''

        resp = self.client.post(
            self.url,
            self.valid_email
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_invalid_username(self):
        '''Failed, bad username'''

        resp = self.client.post(
            self.url,
            self.invalid_username
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_password(self):
        '''Failed invalid password'''

        resp = self.client.post(
            self.url,
            self.invalid_password
        )
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_email(self):
        '''Failed, invalid email'''

        resp = self.client.post(
            self.url,
            self.invalid_email
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_view(self):
        '''Resolves login view'''
        
        self.assertEqual(self.login_view.func.view_class, LoginAPIView)

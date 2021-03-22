from rest_framework.test import APITestCase
from django.test import RequestFactory
from authentication.models import User
from django.urls import reverse, resolve
from rest_framework import status

from authentication.views import SignupAPIView

class TestSetUp(APITestCase):
    def setUp(self):
        self.url = reverse('authentication:signup')
        self.signup_view = resolve(self.url)
        self.valid_user = {
            'username': 'testuser',
            'email': "test@user.io",
            'password': 'test@user',
            'phone_number': '231895049034',
            'firstname': 'namefirst',
            'lastname': 'namelast'
        }

        self.bad_email = {
            'username': 'testuser',
            'email': "test",
            'password': 'test@user',
            'phone_number': '231895049034',
            'firstname': 'namefirst',
            'lastname': 'namelast'
        }

        self.bad_password = {
            'username': 'testuser',
            'email': "test@user.io",
            'password': 'test@user',
            'phone_number': '231895049034',
            'firstname': 'namefirst',
            'lastname': 'namelast'
        }
        self.bad_username = {
            'username': 'testuser'*100,
            'email': "test@user.io",
            'password': 'test@user',
            'phone_number': '231895049034',
            'firstname': 'namefirst',
            'lastname': 'namelast'
        }

        self.missing_fields = {
            'username': 'testuser',
            'email': "test@user.io",
            'password': 'test@user',
            'firstname': 'namefirst',
            'lastname': 'namelast'
        }

        self.empty_fields = {
            'username': '',
            'email': "test@user.io",
            'password': 'test@user',
            'phone_number': '231895049034',
            'firstname': 'namefirst',
            'lastname': 'namelast'
        }


class TestSignupAPI(TestSetUp):
    def test_valid_user(self):
        ''' Successful signup'''

        resp = self.client.post(
            self.url,
            self.valid_user,
            format='json'
        )
        user = User.objects.get(username=self.valid_user['username'])
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.is_active == False)
        self.assertEqual(
            resp.message, "Check your email to confirm registration")

        # Test duplicate signup
        resp2 = self.client.post(
            self.url,
            self.valid_user,
            format='json'
        )
        self.assertEqual(resp2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_username_validation(self):
        '''Username validation fails'''

         resp = self.client.post(
            self.url,
            self.bad_username,
            format='json'
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_email_validation(self):
        '''Email validation fails'''

         resp = self.client.post(
            self.url,
            self.bad_email,
            format='json'
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_password_validation(self):
        '''Email validation fails'''

         resp = self.client.post(
            self.url,
            self.bad_password,
            format='json'
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)


    def test_missing_fields(self):
        '''Failed signup'''

         resp = self.client.post(
            self.url,
            self.missing_fields,
            format='json'
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

     def test_empty_fields(self):
        '''Failed signup'''
         resp = self.client.post(
            self.url,
            self.empty_fields,
            format='json'
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_signup_view(self):
        '''Resolves the api view'''
        self.assertEqual(self.signup_view.func.view_class, SignupAPIView)

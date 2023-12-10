# '''
# Views Test Suite
# Testing can be ran using the following command
# (assuming you are in an activated virtual environment):
# ./manage.py test API
# '''
# from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import authenticate, login
from main_app.forms import CreateNewUser, loginForm

class ViewTest(TestCase):
    '''Class for Views'''

    def setUp(self):
        self.user = User.objects.create(
            username = "Alex",
            email = "Alex@test.com",
            password = "test"
        )
        self.client.force_login(user = self.user)

    def test_models_smoke_test(self):
        '''smoke test'''
        self.assertEqual(1, 1) 

    def test_welcome(self):
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/welcome.html')

    def test_drills(self):
        response = self.client.post(reverse('drills'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/Drills/drills.html')

    def test_Fundamentals(self):
        response = self.client.post(reverse('Fundamentals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/Drills/fundamentals.html')

    def test_Shotmaking(self):
        response = self.client.post(reverse('Shotmaking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/Drills/Shotmaking.html')

    def test_Kicking(self):
        response = self.client.post(reverse('Kicking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/Drills/kicking.html')

    def test_Banking(self):
        response = self.client.post(reverse('Banking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/Drills/banking.html')

    def test_Safety(self):
        response = self.client.post(reverse('Safety'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/Drills/Safety.html')

    def test_Jumping(self):
        response = self.client.post(reverse('Jumping'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_app/Drills/Jumping.html')


class createTestCase(TestCase):
    
    def test_create(self):
        form_data = {
            'username': 'Todd',
            'email': 'Todd@test.com',
            'password': 'test',
        }

        form = CreateNewUser(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post('/create/', form_data)
        self.assertEqual(response.status_code, 302)
        
        user = User.objects.get(username='Todd')
        self.assertIsNotNone(user)
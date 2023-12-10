'''
URL Test Suite

Tests URL availability and non-data producing/consuming view rendering.

Testing can be ran using the following command 
(assuming you are in an activated virtual environment):
./manage.py test API
'''

# from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve

# Create your tests here.


class TestUrls(TestCase):
    '''git 
    Testing application URL's to ensure that they behave correctly
    when the user is NOT authenticated
    '''

    def test_url_smoke_test(self):
        """Smoke test"""
        self.assertEqual(1, 1)

    # Testing Endpoints

    def test_url_welcome(self):
        """Test access to the root url"""
        response = self.client.get(reverse("welcome"))
        self.assertEqual(response.status_code, 200)

    def test_url_(self):
        """Test access to the root url"""
        response = self.client.get(reverse("create"))
        self.assertEqual(response.status_code, 200)

    def test_url_login(self):
        """Test access to the root url"""
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_url_drills(self):
        """Test access to the root url"""
        response = self.client.get(reverse("drills"))
        self.assertEqual(response.status_code, 302)

    def test_url_Fundamentals(self):
        """Test access to the root url"""
        response = self.client.get(reverse("Fundamentals"))
        self.assertEqual(response.status_code, 302)

    def test_url_Shotmaking(self):
        """Test access to the root url"""
        response = self.client.get(reverse("Shotmaking"))
        self.assertEqual(response.status_code, 302)

    def test_url_Kicking(self):
        """Test access to the root url"""
        response = self.client.get(reverse("Kicking"))
        self.assertEqual(response.status_code, 302)

    def test_url_Banking(self):
        """Test access to the root url"""
        response = self.client.get(reverse("Banking"))
        self.assertEqual(response.status_code, 302)

    def test_url_Safety(self):
        """Test access to the root url"""
        response = self.client.get(reverse("Safety"))
        self.assertEqual(response.status_code, 302)

    def test_url_Jumping(self):
        """Test access to the root url"""
        response = self.client.get(reverse("Jumping"))
        self.assertEqual(response.status_code, 302)

    def test_url_stop(self):
        """Test access to the root url"""
        response = self.client.get(reverse("stop"))
        self.assertEqual(response.status_code, 302)

    def test_url_follow(self):
        """Test access to the root url"""
        response = self.client.get(reverse("follow"))
        self.assertEqual(response.status_code, 302)

    def test_url_draw(self):
        """Test access to the root url"""
        response = self.client.get(reverse("draw"))
        self.assertEqual(response.status_code, 302)

    def test_url_mightyx_stun(self):
        """Test access to the root url"""
        response = self.client.get(reverse("mightyx_stun"))
        self.assertEqual(response.status_code, 302)

    def test_url_mightyx_follow(self):
        """Test access to the root url"""
        response = self.client.get(reverse("mightyx_follow"))
        self.assertEqual(response.status_code, 302)

    def test_url_mightyx_draw(self):
        """Test access to the root url"""
        response = self.client.get(reverse("mightyx_draw"))
        self.assertEqual(response.status_code, 302)

    def test_url_mill(self):
        """Test access to the root url"""
        response = self.client.get(reverse("mill"))
        self.assertEqual(response.status_code, 302)

    def test_url_everest(self):
        """Test access to the root url"""
        response = self.client.get(reverse("everest"))
        self.assertEqual(response.status_code, 302)

    def test_url_ladder(self):
        """Test access to the root url"""
        response = self.client.get(reverse("ladder"))
        self.assertEqual(response.status_code, 302)

    def test_url_corner(self):
        """Test access to the root url"""
        response = self.client.get(reverse("corner"))
        self.assertEqual(response.status_code, 302)
        
    def test_url_train(self):
        """Test access to the root url"""
        response = self.client.get(reverse("train"))
        self.assertEqual(response.status_code, 302)

    def test_url_follower(self):
        """Test access to the root url"""
        response = self.client.get(reverse("follower"))
        self.assertEqual(response.status_code, 302)
    
    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("three_rail_kick"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("one_rail_kick"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("two_rail_kick"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("kicking1"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("kicking2"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("kicking3"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("one_rail_bank"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("two_rail_bank"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("three_rail_bank"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("four_rail_bank"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("banking1"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("banking2"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("safety1"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("safety2"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("safety3"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("safety4"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("safety5"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("safety6"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("jumping1"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("jumping2"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("jumping3"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("jumping4"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("jumping5"))
        self.assertEqual(response.status_code, 302)

    def test_url_logout(self):
        """Test access to the root url"""
        response = self.client.get(reverse("jumping6"))
        self.assertEqual(response.status_code, 302)
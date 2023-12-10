# '''
# Model Test Suite
# Testing can be ran using the following command 
# (assuming you are in an activated virtual environment):
# ./manage.py test API
# '''

from main_app.models import User
from main_app.models import Stats
from main_app.models import Drill_data
from django.test import TestCase

# from API.models import CreateRecipe, RecipeSearch


class ModelTest(TestCase):
    '''
    Tests model saving functionality for models found in models.py
    '''
    def setUp(self):
        '''Global setup to create a user account'''
        self.user = user = User.objects.create(
            username="Jake",
            email="Jake@test.com",
            password="test")
        
        self.data = Stats.objects.create(
            userStats = user,
            drillsComplete = 4
        )
        self.drill = Drill_data.objects.create(
            username = user.username,
            amount_completed = 4
        )

    def test_models_smoke_test(self):
        '''smoke test'''
        self.assertEqual(1, 1) 

    def test_name_return(self):
        self.assertEqual("Jake", self.user.__str__())

    def test_email_return(self):
        self.assertEqual("Jake@test.com", self.user.give_email())

    def test_stats_return(self):
        self.assertEqual(4,self.data.__int__())
        
    def test_data_return(self):
        self.assertEqual(4,self.drill.__int__())
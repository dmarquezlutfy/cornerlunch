from django.test import TestCase
from .models import User

import os


class UsersTestCase(TestCase):


    def setUp(self):
        User.objects.create_user('food_manager', email='food@manager.com', password='test')

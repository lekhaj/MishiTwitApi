from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from mishi_tweet_api import models

def sample_user(email='test@mishipay.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

class ModelTests(TestCase):

	
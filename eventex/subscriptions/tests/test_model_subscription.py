from django.test import TestCase
from datetime import datetime

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Alan maik',
            cpf='12345678901',
            email='alanmaikm@gmail.com',
            phone='73-999558094'
        )
        self.obj.save()
    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
       """Subscription must have an auto created_at attr"""
       self.assertIsInstance(self.obj.created_at, datetime)
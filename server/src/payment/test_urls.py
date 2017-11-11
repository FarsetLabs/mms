from django.test import TestCase
from django.urls import resolve

from .views import index


class TestPaymentIndex(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/payment/')
        self.assertEqual(found.func, index)

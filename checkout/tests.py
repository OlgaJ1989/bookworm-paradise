""" Automated testing """
from django.test import TestCase
from django.urls import resolve, reverse
from .views import cache_checkout_data, checkout


class TestUrls(TestCase):
    """ Test urls.py """

    def test_cache_checkout_data_url_renders_cache_checkout_data_view(self):
        """
        Test 'home' url is working and rendering 'home' view.
        """
        url = reverse('cache_checkout_data')
        print(resolve(url))
        self.assertEqual(resolve(url).func, cache_checkout_data)

    def test_checkout_url_renders_checkout_view(self):
        """
        Test 'checkout' url is working and rendering 'checkout' view.
        """
        url = reverse('checkout')
        print(resolve(url))
        self.assertEqual(resolve(url).func, checkout)

""" Automated testing """
from django.test import TestCase
from django.urls import resolve, reverse
from .views import profile


class TestUrls(TestCase):
    """ Test urls.py """

    def test_profile_url_renders_profile_view(self):
        """
        Test 'profile' url is working and rendering 'profile' view.
        """
        url = reverse('profile')
        print(resolve(url))
        self.assertEqual(resolve(url).func, profile)

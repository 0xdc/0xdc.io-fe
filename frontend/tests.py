from django.test import TestCase, RequestFactory
from django.urls import reverse

from .views import homepage
from django.contrib.auth.models import User

class HomepageTests(TestCase):

    # setUp before every test
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get(reverse("index"))

    def test_homepage(self):
        response = homepage(self.request)
        self.assertNotContains(response, "/admin")

    def test_homepage_as_admin(self):
        admin = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        self.request.user = admin
        response = homepage(self.request)
        self.assertContains(response, "/admin")

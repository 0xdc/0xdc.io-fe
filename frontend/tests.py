from django.test import TestCase, RequestFactory
from django.urls import reverse

from .views import homepage
from django.contrib.auth.models import User

class HomepageTests(TestCase):

    # setUp before every test
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get(reverse("frontend:index"))

    def test_homepage(self):
        response = homepage(self.request)
        self.assertNotContains(response, "/admin")
        # Just for this test, ensure the view uses the correct template
        self.assertIn("frontend/index.html", response.template_name)

    def test_homepage_as_admin(self):
        admin = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        self.request.user = admin
        response = homepage(self.request)
        self.assertContains(response, "/admin")

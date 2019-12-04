from django.test import SimpleTestCase
from django.urls import reverse, resolve


from accounts.views import login_user, logout_user, user_registration


class TestUrls(SimpleTestCase):

    def test_login_user_url_resolves(self):
        url = reverse('accounts:login')
        self.assertEquals(resolve(url).func, login_user)

    def test_logout_user_url_resolves(self):
        url = reverse('accounts:logout')
        self.assertEquals(resolve(url).func, logout_user)

    def test_user_registration_url_resolves(self):
        url = reverse('accounts:register')
        self.assertEquals(resolve(url).func, user_registration)

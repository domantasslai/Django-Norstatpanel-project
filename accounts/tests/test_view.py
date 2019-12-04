from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client

class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.register_url = reverse('accounts:register')
        self.logout_url = reverse('accounts:logout')
        user = User.objects.create(username = 'domantas', email='domantas@gmail.com', password='password')

    def testLogin(self):
        response = self.client.get(self.login_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def testLogout(self):
        response = self.client.get(self.logout_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def testRegister(self):
        response = self.client.get(self.register_url, follow=True)
        self.assertEqual(response.status_code, 200)

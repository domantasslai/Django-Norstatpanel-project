from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase, Client


from polls.models import Poll, Choice, Vote
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('polls:list')
        self.add_poll_url = reverse('polls:add')
        self.edit_poll_url = reverse('polls:edit_poll', kwargs={'poll_id': 5})
        self.add_choice_url = reverse('polls:add_choice', kwargs={'poll_id': 5})
        self.edit_choice_url = reverse('polls:edit_choice', kwargs={'choice_id': 1})

        self.choice_confirm_delete_url = reverse('polls:choice_confirm_delete', kwargs={'choice_id': 5})
        self.poll_confirm_delete_url = reverse('polls:poll_confirm_delete', kwargs={'poll_id': 5})

        self.detail_url = reverse('polls:detail', kwargs={'poll_id': 5})
        self.vote_url = reverse('polls:vote', kwargs={'poll_id': 5})
        user = User.objects.create(username = 'domantas', email='domantas@gmail.com', password='password')
        self.poll1 = Poll.objects.get_or_create(
            owner = user,
            text = 'asdasdasda',
            pub_date='2019-11-17'
        )


    def test_project_list_GET(self):
        response = self.client.get(self.list_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_add_poll_GET(self):
        response = self.client.get(self.add_poll_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_edit_poll_GET(self):
        response = self.client.get(self.edit_poll_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_add_choice_GET(self):
        response = self.client.get(self.add_choice_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_edit_choice_GET(self):
        response = self.client.get(self.poll_confirm_delete_url, follow=True)
        self.assertEqual(response.status_code, 200)

    # def test_choice_confirm_delete_GET(self):
    #     response = self.client.get(self.choice_confirm_delete_url)
    #     self.assertEqual(response.status_code, 200)

    def test_poll_confirm_delete_choice_GET(self):
        response = self.client.get(self.poll_confirm_delete_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_detail_GET(self):
        response = self.client.get(self.detail_url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_vote_GET(self):
        response = self.client.get(self.vote_url, follow=True)
        self.assertEqual(response.status_code, 200)

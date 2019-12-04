from django.test import SimpleTestCase
from django.urls import reverse, resolve

from polls.views import polls_list, add_poll, edit_poll, add_choice, edit_choice, delete_choice, delete_poll, polls_detail, poll_vote

class TestUrls(SimpleTestCase):

    # 9 Testai
    def test_list_url_resolves(self):
        url = reverse('polls:list')
        self.assertEquals(resolve(url).func, polls_list)

    def test_add_url_resolves(self):
        url = reverse('polls:add')
        self.assertEquals(resolve(url).func, add_poll)

    def test_edit_poll_url_is_resolves(self):
        path = reverse('polls:edit_poll', kwargs={'poll_id': 5})
        self.assertEquals(resolve(path).func, edit_poll)

    def test_add_choice_url_is_resolves(self):
        path = reverse('polls:add_choice', kwargs={'poll_id': 5})
        self.assertEquals(resolve(path).func, add_choice)

    def test_edit_choice_url_is_resolves(self):
        path = reverse('polls:edit_choice', kwargs={'choice_id': 1})
        self.assertEquals(resolve(path).func, edit_choice)

    def test_choice_confirm_delete_url_is_resolves(self):
        path = reverse('polls:choice_confirm_delete', kwargs={'choice_id': 1})
        self.assertEquals(resolve(path).func, delete_choice)

    def test_poll_confirm_delete_url_is_resolves(self):
        path = reverse('polls:poll_confirm_delete', kwargs={'poll_id': 1})
        self.assertEquals(resolve(path).func, delete_poll)

    def test_detail_url_is_resolves(self):
        path = reverse('polls:detail', kwargs={'poll_id': 5})
        self.assertEquals(resolve(path).func, polls_detail)

    def test_poll_vote_url_is_resolves(self):
        path = reverse('polls:vote', kwargs={'poll_id': 5})
        self.assertEquals(resolve(path).func, poll_vote)

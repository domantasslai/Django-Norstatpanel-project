from django.contrib.auth.models import User
from django.db import models

class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    text = models.CharField(max_length=255)
    pub_date = models.DateField()

    def __str__(self):
        return self.text

    def user_can_vote(self, user):
        # Returns False is user has already voted, else True
        user_votes = user.vote_set.all()
        qs = user_votes.filter(poll=self)
        if qs.exists():
            return False
        return True

    @property
    def num_votes(self):
        return self.vote_set.count()


    def get_result_dict(self):
        res = []
        for choice in self.choice_set.all():
            d = {}
            d['text'] = choice.choice_text
            d['num_votes'] = choice.num_votes
            if not self.num_votes:
                d['percentage'] = 0
            else:
                d['percentage'] = choice.num_votes / self.num_votes * 100
            res.append(d)
        return res

    def get_pdf(self):
        res = []
        for choice in self.choice_set.all():
            d={}
            d['text'] = self.text
            d['choice_text'] = choice.choice_text
            res.append(d)
        return res



class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.poll.text[:100], self.choice_text[:100])

    @property
    def num_votes(self):
        return self.vote_set.count()



class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

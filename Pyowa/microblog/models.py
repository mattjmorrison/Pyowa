from django.db import models
from django.contrib.auth.models import User

class Microblog(models.Model):
    poster = models.ForeignKey(User)
    title = models.CharField(max_length=10)
    message = models.CharField(max_length=100)
    posted_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.poster.username + ": " + self.message
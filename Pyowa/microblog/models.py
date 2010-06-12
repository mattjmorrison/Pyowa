from django.db import models
from django.contrib.auth.models import User

class Microblog(models.Model):
    poster = models.ForeignKey(User)
    message = models.CharField(max_length=100)
    posted_time = models.DateTimeField(auto_now=True)


from django.db import models
from django.contrib.auth.models import User

class PermissionGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(User, null=True)

    def __unicode__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(User, null=True)
    permissions = models.ForeignKey(PermissionGroup, null=True)

    def __unicode__(self):
        return self.name

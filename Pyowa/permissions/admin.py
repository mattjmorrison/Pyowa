from django.contrib import admin
from Pyowa.permissions import models

admin.site.register(models.Permission)
admin.site.register(models.PermissionGroup)
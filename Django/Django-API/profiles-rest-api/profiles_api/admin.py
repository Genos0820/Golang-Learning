from django.contrib import admin # type: ignore

from profiles_api import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
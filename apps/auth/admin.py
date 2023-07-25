from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group, User as DefaultUser

admin.site.unregister(Group)
admin.site.unregister(DefaultUser)

admin.site.register(User)

from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin


admin.site.register(Profile)
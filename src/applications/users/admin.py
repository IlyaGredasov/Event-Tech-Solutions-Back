from applications.api.admin import register_app_models
from applications.users.apps import UsersConfig
from applications.users.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
register_app_models(UsersConfig.name)

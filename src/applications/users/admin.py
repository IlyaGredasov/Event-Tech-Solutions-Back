from applications.api.admin import register_app_models
from applications.users.apps import UsersConfig
from applications.users.forms import CustomUserCreationForm
from applications.users.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            {
                'fields': (
                    'job',
                    'avatar',
                    'vk',
                    'telegram',
                    'mail',
                    'phone_number',
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)
register_app_models(UsersConfig.name)

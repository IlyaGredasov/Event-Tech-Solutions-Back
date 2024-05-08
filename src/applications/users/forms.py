from django.contrib.auth.forms import UserCreationForm

from applications.users.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

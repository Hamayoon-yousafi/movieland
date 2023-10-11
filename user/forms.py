from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomLoginForm(AuthenticationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs):
        super().__init__(request, *args, **kwargs)

        for label, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control bg-dark text-white customize-input p-0 ps-2 mb-2', 'placeholder': 'Enter ' + label.title()})

    
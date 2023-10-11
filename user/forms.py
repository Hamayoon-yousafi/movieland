from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


CSS_CLASS = 'form-control bg-dark text-white customize-input p-0 ps-2 mb-2'
LABELS = {'username': 'Username', 'password1': 'Password', 'password2': 'Confirm Password', 'email': 'Email'}

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, label in LABELS.items():
            self.fields[field_name].label = label
            self.fields[field_name].widget.attrs.update({'class': CSS_CLASS, 'placeholder': label, 'autofocus': False})

    class Meta:
        model = User
        fields = ('username', 'email')


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for label, field in self.fields.items():
            field.widget.attrs.update({'class': CSS_CLASS, 'placeholder': 'Enter ' + label.title()})

    
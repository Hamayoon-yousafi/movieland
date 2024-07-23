from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


CSS_CLASSES = 'form-control bg-dark text-white customize-input p-0 ps-2 mb-2'
LABELS = {'username': 'Username', 'password1': 'Password', 'password2': 'Confirm Password', 'email': 'Email'}

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, label in LABELS.items():
            self.fields[field_name].label = label
            self.fields[field_name].widget.attrs.update({'class': CSS_CLASSES, 'placeholder': label, 'autofocus': False})

    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture', 'favorite_genre')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['profile_picture'].widget.attrs.update({'class': 'form-control bg-dark text-white'})
        self.fields['favorite_genre'].widget.attrs.update({'class': 'form-select bg-dark text-white'})

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for label, field in self.fields.items():
            field.widget.attrs.update({'class': CSS_CLASSES, 'placeholder': 'Enter ' + label.title()})

    
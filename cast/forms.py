from django import forms
from .models import Cast


class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
        }
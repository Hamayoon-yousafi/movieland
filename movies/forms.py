from django import forms 
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            ),
            'tag_ids': forms.CheckboxSelectMultiple(),
            'genre_ids': forms.CheckboxSelectMultiple(),
        }
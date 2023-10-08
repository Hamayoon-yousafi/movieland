from django import forms 
from .models import Movie, Review


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


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = 'user_id', 'movie_id'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for label, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control custom-review-input bg-dark text-white'})
            if label == 'body':
                field.widget.attrs.update({'placeholder': 'Write your review for this movie.', 'id': 'review-body', 'rows': 1}) 
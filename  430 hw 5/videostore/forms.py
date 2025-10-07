from django import forms
from .models import Movie
import datetime

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'movie_id', 'title', 'actor1_name', 'actor2_name',
            'director_name', 'genre', 'release_year',
        ]
        widgets = {
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'release_year': forms.NumberInput(attrs={'min': 1888, 'class': 'form-control'}),
        }

    def clean_release_year(self):
        y = self.cleaned_data['release_year']
        if y < 1888 or y > datetime.date.today().year + 1:
            raise forms.ValidationError('Enter a realistic release year.')
        return y

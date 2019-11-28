from django.forms import ModelForm
from .models import Movie, Genre, Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['content']
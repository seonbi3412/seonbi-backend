from django.contrib import admin
from .models import Movie, Genre, Review, Actor, Article

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Actor)
admin.site.register(Article)
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('genres/', views.genre_index, name='genre_index'),
    path('actors/', views.actors_index, name='actors_index'),
    path('actors/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    path('actors/<int:actor_pk>/like/', views.actor_like, name='actor_like'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/like/', views.like_movie, name='like_movie'),
    path('<int:movie_pk>/reviews/', views.movie_reviews, name='movie_reviews'),
    path('reviews/', views.review, name='review'),
    path('articles/', views.article, name='article'),
    path('reviews/<int:review_pk>/', views.update_delete, name='update_delete'),
    path('articles/<int:review_pk>/', views.update, name='update'),
    path('users/<int:user_pk>/', views.user_detail),
    path('users/', views.user_index, name='user_index'),
    path('users/<int:user_pk>/update_delete/', views.user_update_delete, name='user_update_delete'),
    path('recommend/', views.recommend, name='recommend')
]
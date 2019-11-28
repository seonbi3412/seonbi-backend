from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='account_signup'),
    path('update/<int:user_pk>/', views.update, name='account_update'),
]
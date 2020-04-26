from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('user_cards/', views.user_cards, name='user_cards'),
]
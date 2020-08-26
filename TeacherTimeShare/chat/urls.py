from django.urls import path

from .views import enter_class, room

urlpatterns = [
    path('', enter_class, name='enter_class'),
    path('<int:pk>/', room, name='room'),
]
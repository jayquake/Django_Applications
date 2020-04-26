from . import views
from django.urls import path

urlpatterns = [
    path('pokedex/', views.pokedex, name='pokedex'),
    path('card_sale/', views.card_sale, name='card-sale'),
    path('card_confirm_sale/<int:pk>/', views.card_confirmation, name='card_confirm_sale'),
    path('card_confirm_buy/<int:card_id>/', views.card_confirm_buy, name='card_confirm_buy'),
]
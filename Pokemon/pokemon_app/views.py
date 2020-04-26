from django.core.validators import MaxValueValidator
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from account_app.models import Profile
from .forms import SellCardForm,BuyCardForm
from .models import Card, CardSale, Deck, CardBuy


def pokedex(request):
    cards = Card.objects.all()
    return render(request, 'pokedex.html',{'cards': cards})


def card_confirmation(request, pk):
    card = Card.objects.get(id=pk)
    deck = request.user.profile.deck
    if request.method == 'POST':
        form = SellCardForm(request.POST)
        if form.is_valid():
            card_on_sale = form.save(commit=False)
            card_on_sale.card = card
            card_on_sale.profile = request.user.profile
            card_on_sale.save()
            deck.cards.remove(card)
            return redirect('card-sale')
    form = SellCardForm()
    return render(request, 'card_confirm_sale.html', {'form':form, 'card':card})


def card_sale(request):
    card_sold = CardSale.objects.all()
    return render(request, 'card_sale.html', {'cards': card_sold})


def card_confirm_buy(request, card_id):
    card = CardSale.objects.get(card_id=card_id)
    deck = request.user.profile.deck
    cards_sold = CardSale.objects.all()
    if request.method == 'POST':
        form = BuyCardForm(request.POST)
        if form.is_valid():
            card_to_buy = form.save(commit=False)
            Card.pk = card.card_id
            card_to_buy.card = card
            card_to_buy.profile = request.user.profile
            card_card = Card.objects.get(pk=card.card_id)
            deck.save(card)
            cards_sold.remove(card)
            return redirect('card-sale')
    form = BuyCardForm()
    return render(request, 'card_confirm_buy.html', {'cards': cards_sold, 'form': form})


# class CardSaleView(DetailView):
#     model = CardSale
#     form_class = SellCardForm
#     template_name = 'card_sale.html'
#
#     def card_to_sell(request):
#         # self.request.user.profile.deck.cards.remove()
#         context ={
#             'cards': CardSale.objects.all(),
#             'form': SellCardForm
#         }
#         return render(request, 'card_sale.html', context)
#
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.pk_url_kwarg = None
#
#     def get_object(self, queryset=None):
#         return self.request.user.profile.deck.cards.get(id=self.kwargs['pk'])
#
# class CardConfirmSale(DetailView):
#     def card_to_sell(request):
#         context ={
#             'cards':request.pk_url_kwarg
#         }
#         return render(request, 'card_confirm_sale.html', context)
#
#     def get_object(self, queryset=None):
#         return self.request.user.profile.deck.cards.get(id=self.kwargs['pk'])
#
# def buy(request, pk):
#     sale = CardSale.objects.filter(pk=pk)
#     if sale.exists():
#         sale = sale[0]
#         profile = request.user.profile
#         if profile.points < sale.price:
#             messages.warning(request, message='you broke')
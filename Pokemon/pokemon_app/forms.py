from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CardSale ,CardBuy


class SellCardForm(forms.ModelForm):
    class Meta:
        model = CardSale
        fields = ['price']


class BuyCardForm(forms.ModelForm):
    class Meta:
        model = CardBuy
        fields = ['price']
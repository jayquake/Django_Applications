from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateFrom, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from random import randint
from pokemon_app.models import Card, Deck


# Create your views here.

def home(request):
    return render(request, 'home.html')


@login_required
def user_cards(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    deck, created = Deck.objects.get_or_create(profile=user_profile)
    if user_profile.deck.cards.all().count() == 0 or user_profile.deck.cards.all().count() < 5:
        for x in range(5):
            num = randint(1, Card.objects.all().count())
            card = Card.objects.get(id=num)
            deck.cards.add(card)

    context = {
        'points': sum([card.attack for card in deck.cards.all()]),
        'cards': deck.cards.all()
    }
    return render(request, 'user_cards.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    messages.success(request, f'Generating your Cards!')
    deck, created = Deck.objects.get_or_create(profile=user_profile)
    if user_profile.deck.cards.all().count() == 0:
        for x in range(5):
            num = randint(1, Card.objects.all().count())
            card = Card.objects.get(id=num)
            deck.cards.add(card)
        messages.success(request, f'Your free cards have been generated')
    if request.method == "POST":
        u_form = UserUpdateFrom(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateFrom(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,

    }
    return render(request, 'profile.html', context)
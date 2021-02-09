from django import forms
from django.db import transaction
from .models import User, ContributorProfile, DownloaderProfile
from django.contrib.auth.forms import UserCreationForm


class ContributorRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_contributor = True
        if commit:
            user.save()
        return user


class ContributorUpdateFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ContributorProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ContributorProfile
        fields = ['image', 'first_name', 'last_name', 'email']


class DownloaderRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_downloader = True
        if commit:
            user.save()
        return user


class DownloaderUpdateFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class DownloaderProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = DownloaderProfile
        fields = ['first_name', 'last_name']

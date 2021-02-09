from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import ContributorRegisterForm, DownloaderRegisterForm, ContributorProfileUpdateForm, \
    DownloaderProfileUpdateFrom, ContributorUpdateFrom, DownloaderUpdateFrom
from accounts.models import User, ContributorProfile, DownloaderProfile


def registration_home(request):
    context = {
    }
    return render(request, 'accounts/Registration.html')


class ContributorRegisterView(CreateView):
    context = {
        'form': ContributorRegisterForm
    }
    model = User
    form_class = ContributorRegisterForm
    template_name = 'accounts/register_contributor.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'contributor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class DownloaderRegisterView(CreateView):
    model = User
    form_class = DownloaderRegisterForm
    template_name = 'accounts/register_downloader.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'downloader'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


def profile(request):
    if request.user.is_contributor:
        user_profile, created = ContributorProfile.objects.get_or_create(user=request.user)
        if request.method == 'GET':
            user_profile, created = ContributorProfile.objects.get_or_create(user=request.user)
        if request.method == "POST":
            contributor_update_form = ContributorUpdateFrom(request.POST, instance=request.user.contributorprofile)
            contributor_profile_form = ContributorProfileUpdateForm(request.POST, request.FILES,
                                                                    instance=request.user.contributorprofile)
            if contributor_update_form.is_valid() or contributor_profile_form.is_valid():
                first = contributor_update_form.cleaned_data['first_name']
                last = contributor_update_form.cleaned_data['last_name']
                email = contributor_update_form.cleaned_data['email']

                request.user.first_name = first
                request.user.last_name = last
                request.user.email = email
                request.user.save()
                contributor_update_form.save()
                contributor_profile_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')
        else:
            contributor_update_form = ContributorUpdateFrom(instance=request.user.contributorprofile)
            contributor_profile_form = ContributorProfileUpdateForm(instance=request.user.contributorprofile)
        context = {
            'u_form': contributor_update_form,
            'p_form': contributor_profile_form,

        }
        return render(request, 'accounts/profile/contributor_profile.html', context)
    # CREATING Student USERS
    elif request.user.is_downloader:
        if request.method == 'GET':
            user_profile, created = DownloaderProfile.objects.get_or_create(user=request.user)
        if request.method == "POST":
            downloader_update_form = DownloaderUpdateFrom(request.POST, instance=request.user.downloaderprofile)
            downloader_profile_form = DownloaderProfileUpdateFrom(request.POST, request.FILES,
                                                                  instance=request.user.downloaderprofile)
            if downloader_update_form.is_valid() or downloader_profile_form.is_valid():
                downloader_profile_form.save()
                downloader_update_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')
        else:
            downloader_update_form = DownloaderUpdateFrom(instance=request.user.downloaderprofile)
            downloader_profile_form = DownloaderProfileUpdateFrom(instance=request.user.downloaderprofile)
        context = {
            'u_form': downloader_update_form,
            'p_form': downloader_profile_form,

        }
        return render(request, 'accounts/profile/downloader_profile.html', context)
    return

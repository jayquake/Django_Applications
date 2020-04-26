from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse

from account_app.models import Profile
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from pokemon_app.models import Card ,Deck


@login_required
def forum(request):

    user_profile = Profile.objects.get(user=Post.objects.author)
    deck = Deck.objects.get(profile=user_profile)

    context = {
        'posts': Post.objects.all(),
        'points': sum([card.attack for card in Post.author.deck.cards.all()]),
    }
    return render(request, 'forum.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'forum.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/forum/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def user_posts(request):
    user = Post.objects.filter(author=request.user)
    context = {
        'posts': user.all().order_by('-date_posted')
    }
    return render(request, 'user_posts.html', context)
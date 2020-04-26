from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from . import forms
from account_app.models import User
from .forms import UpdateCommentForm
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def forum(request):

    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'forum/forum.html', context)

# POSTS
class PostListView(ListView):
    model = Post
    template_name = 'forum/forum.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'forum/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


def post_detail(request, pk):
    template_name = 'forum/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    new_comment = None

    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            author_id = request.user.pk
            post_id = post.pk
            comment = form.cleaned_data.get('content')
            comm = Comment(content=comment, author_id=author_id, post_id=post_id)
            print(comm)
            comm.save()
            messages.success(request, f'Comment Posted')
            return redirect('.')
    else:
        form = forms.CommentForm()

        context = {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'form': form
                   }

    return render(request, template_name, context)


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

# COMMENTS
def my_posts(request):
    user = Post.objects.filter(author=request.user)
    context = {
        'posts': user.all().order_by('-date_posted')
    }
    return render(request, 'forum/my_posts.html', context)


def comment_delete_confirmation(request, post_id, pk):
    comment_to_delete = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment_to_delete.post_id)
    if request.method == "GET":
        pass
    if request.method == "POST":
        if request.user.is_teacher:
            post_id = Post.objects.get(pk=comment_to_delete.post_id)
            comment_to_delete.teacherprofile = request.user.teacherprofile
            print(post)
            print(post_id)
            Post.delete(comment_to_delete)
            return redirect(f'/forum/post/{comment_to_delete.post_id}')

        elif request.user.is_student:
            post_id = Post.objects.get(pk=comment_to_delete.post_id)
            comment_to_delete.studentprofile = request.user.studentprofile
            print(post)
            print(post_id)
            Post.delete(comment_to_delete)
            return redirect(f'/forum/post/{comment_to_delete.post_id}')

    context = {'comment': comment_to_delete,
               'post': post,
               'post_id': post_id,
               }
    return render(request, 'forum/comment_confirm_delete.html', context)


def comment_update_confirmation(request, post_id, pk):
    old_comment = get_object_or_404(Comment, pk=pk)
    if request.method == "GET":
        form = forms.UpdateCommentForm(request.POST)
        pass
    if request.method == "POST":
        form = forms.UpdateCommentForm(request.POST)
        if form.is_valid():
            author_id = request.user.pk
            post_id = old_comment.post_id
            comment_id = old_comment.pk
            new_comment = form.cleaned_data.get('content')
            comm = Comment(id=comment_id, content=new_comment, author_id=author_id, post_id=post_id)
            print(comm)
            comm.save()
            messages.success(request, f'Comment Updated')
            return redirect(f'/forum/post/{post_id}')
    else:
        form = forms.CommentForm()

        context = {'old_comment': old_comment,
                   'form': form,
                   'post_id': post_id,
                  }
        return render(request, 'forum/comment_form.html', context)

    # if request.method == 'POST':
    #     form = UpdateCommentForm(request.POST)
    #     if form.is_valid():
    #         comment_to_change = form.save(commit=False)
    #         comment_to_change.content = comment.content
    #         comment_to_change.profile = request.user.profile
    #         comment_to_change.save()
    #         return redirect('../')
    # form = UpdateCommentForm()
    # context = {
    #     'form': form,
    #     'comment': comment,
    # }
    #

    # class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    #     model = Comment
    #     fields = ['content']
    #     success_url = 'post-detail/<:int>'
    #
    #     def form_valid(self, form):
    #         form.instance.author = self.request.user
    #         return super().form_valid(form)
    #
    #     def test_func(self):
    #         comment = self.get_object()
    #         if self.request.user.id == comment.author.id:
    #             return True
    #         return False

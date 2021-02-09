from PIL import Image
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from .models import PostImage, CommentOnPost
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView
from .forms import CommentForm, UpdateCommentForm, UploadForm


def photo_home_view(request):
    context = {
    }
    return render(request, 'picture_app/photo_home_view.html', context)


class UploadView(LoginRequiredMixin, CreateView):
    model = PostImage

    fields = ['title', 'image', 'photo_description']

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.image = None

    def form_valid(self, form):
        form.instance.image_author = self.request.user
        return super().form_valid(form)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img_width = 300
        img_height = 300
        img = Image.open(self.image.path).resize((img_width, img_height))
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)


def post_upload(request):
    template_name = 'picture_app/postimage_form.html'
    user_post = PostImage.objects.create(title=request.user.postimage_set.objects)
    if request.method == 'GET':
        user_post, created = PostImage.objects.get_or_create(image_author=request.user)
    if request.method == "POST":
        contributor_post_form = UploadForm(request.POST, request.FILES, instance=request.user.contributorprofile)
        if contributor_post_form.is_valid():
            title = contributor_post_form.cleaned_data['title']
            photo_description = contributor_post_form.cleaned_data['photo_description']
            image = contributor_post_form.cleaned_data['image']
            image_author_id = request.user.pk
            post_id = user_post.pk
            post_commit = PostImage( title=title, image_author_id=image_author_id, post_id=post_id, image=image.url, photo_description=photo_description)
            print(post_commit)
            post_commit.save()
            messages.success(request, f'Post Uploaded')
            return redirect('.')
    else:
        form = UploadForm()

        context = {'post': user_post,
                   'form': form
                   }

    return render(request, template_name, context)


def post_detail(request, pk):
    template_name = 'picture_app/post_detail.html'
    post = get_object_or_404(PostImage, pk=pk)
    comments = post.comments.all()
    new_comment = None

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            image_image_author_id = request.user.pk
            post_id = post.pk
            comment = form.cleaned_data.get('content')
            comm = CommentOnPost(content=comment, image_image_author_id=image_image_author_id, post_id=post_id)
            print(comm)
            comm.save()
            messages.success(request, f'Comment Posted')
            return redirect('.')
    else:
        form = CommentForm()

        context = {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'form': form
                   }

    return render(request, template_name, context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostImage
    fields = ['title', 'photo_description']

    def form_valid(self, form):
        form.instance.image_image_author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.image_author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostImage
    success_url = 'my-posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.image_author:
            return True
        return False


# COMMENTS
def my_posts(request):
    user = PostImage.objects.filter(image_author=request.user)
    context = {
        'posts': user.all().order_by('-date_posted')
    }
    return render(request, 'picture_app/my_posts.html', context)


def comment_delete_confirmation(request, post_id, pk):
    comment_to_delete = get_object_or_404(CommentOnPost, pk=pk)
    post = get_object_or_404(PostImage, pk=comment_to_delete.post_id)
    if request.method == "GET":
        pass
    if request.method == "POST":
        if request.user.is_contributor:
            post_id = PostImage.objects.get(pk=comment_to_delete.post_id)
            comment_to_delete.contributorprofile = request.user.contributorprofile
            print(post)
            print(post_id)
            PostImage.delete(comment_to_delete)
            return redirect(f'/post/{comment_to_delete.post_id}')

        elif request.user.is_downloader:
            post_id = PostImage.objects.get(pk=comment_to_delete.post_id)
            comment_to_delete.downloaderprofile = request.user.downloaderprofile
            print(post)
            print(post_id)
            PostImage.delete(comment_to_delete)
            return redirect(f'/post/{comment_to_delete.post_id}')

    context = {'comment': comment_to_delete,
               'post': post,
               'post_id': post_id,
               }
    return render(request, 'picture_app/comment_confirm_delete.html', context)


def comment_update_confirmation(request, post_id, pk):
    old_comment = get_object_or_404(CommentOnPost, pk=pk)
    if request.method == "GET":
        form = UpdateCommentForm(request.POST)
        pass
    if request.method == "POST":
        form = UpdateCommentForm(request.POST)
        if form.is_valid():
            image_author_id = request.user.pk
            post_id = old_comment.post_id
            comment_id = old_comment.pk
            new_comment = form.cleaned_data.get('content')
            comm = CommentOnPost(id=comment_id, content=new_comment, image_author_id=image_author_id, post_id=post_id)
            print(comm)
            comm.save()
            messages.success(request, f'Comment Updated')
            return redirect(f'/post/{post_id}')
    else:
        form = CommentForm()

        context = {'old_comment': old_comment,
                   'form': form,
                   'post_id': post_id,
                   }
        return render(request, 'picture_app/comment_form.html', context)

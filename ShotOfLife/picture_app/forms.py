from .models import CommentOnPost, PostImage
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentOnPost
        fields = ('content',)


class UpdateCommentForm(forms.ModelForm):
    class Meta:
        model = CommentOnPost
        fields = ('content',)


class UploadForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('title', 'image', 'photo_description')

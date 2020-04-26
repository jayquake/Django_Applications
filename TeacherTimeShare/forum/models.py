from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from account_app.models import User
from django.urls import reverse

from account_app.models import StudentProfile ,TeacherProfile


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# class CommentDelete(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     post = models.ForeignKey()
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return self.card.name



from PIL import Image
from django.db import models
from django.urls import reverse
from django.utils import timezone

from accounts.models import User


# Create your models here.


class PostImage(models.Model):
    title = models.CharField(max_length=65)
    image = models.ImageField(upload_to='user_uploads')
    photo_description = models.TextField()
    image_author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img_width = 300
        img_height = 300
        img = Image.open(self.image.path).resize((img_width, img_height))
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def __img__(self):
        return self.image

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': self.pk})


class CommentOnPost(models.Model):
    post = models.ForeignKey(PostImage, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.content)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, Model, OneToOneField, CASCADE, ImageField, CharField, FileField, TextField, \
    EmailField
from PIL import Image


# Create your models here.


class User(AbstractUser):
    is_contributor = BooleanField(default=False)
    is_downloader = BooleanField(default=False)


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    image = ImageField(default='default.svg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ContributorProfile(Model):
    first_name = CharField(max_length=20, default='No First Name')
    last_name = CharField(max_length=20, default='No Last Name')
    user = OneToOneField(User, on_delete=CASCADE, default=True)
    image = ImageField(default='default.jpg', upload_to='profile_pics')
    email = EmailField()

    def __str__(self):
        return f"{self.user.username}'s Profile "

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img_width = 300
        img_height = 300
        img = Image.open(self.image.path).resize((img_width, img_height))
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)


class DownloaderProfile(Model):
    first_name = CharField(max_length=20, default='No First Name')
    last_name = CharField(max_length=20, default='No Last Name')
    user = OneToOneField(User, on_delete=CASCADE, default=True)
    image = ImageField(default='default.jpg', upload_to='profile_pics')
    email = EmailField

    def __str__(self):
        return f"{self.user.username}'s Profile "

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img_width = 300
        img_height = 300
        img = Image.open(self.image.path).resize((img_width, img_height))
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)

from django.db.models import *
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.db.models import *
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe
from languages.fields import LanguageField, RegionField
# Create your models here.
import classroom


class User(AbstractUser):
    is_teacher = BooleanField(default=False)
    is_student = BooleanField(default=False)
    is_corporate = BooleanField(default=False)


# class Subject(Model):
#     name = CharField(max_length=30)
#     color = CharField(max_length=7, default='#007bff')
#
#     def __str__(self):
#         return self.name
#
#     def get_html_badge(self):
#         name = escape(self.name)
#         color = escape(self.color)
#         html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
#         return mark_safe(html)


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


class StudentProfile(Model):
    first_name = CharField(max_length=20, default='No First Name')
    last_name = CharField(max_length=20, default='No Last Name')
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    image = ImageField(default='default.jpg', upload_to='profile_pics')
    interests = CharField(max_length=20, default='I dont have one')
    email = EmailField

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class TeacherProfile(Model):
    first_name = CharField(max_length=20, default='No First Name')
    last_name = CharField(max_length=20, default='No Last Name')
    user = OneToOneField(User, on_delete=CASCADE, default=True)
    image = ImageField(default='default.jpg', upload_to='profile_pics')
    resume = FileField(upload_to='resumes')
    about_me = TextField(blank=True)
    job_title = CharField(max_length=15, name='Title')
    languages = LanguageField(max_length=8, blank=True)
    region = RegionField(blank=True)
    email = EmailField

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

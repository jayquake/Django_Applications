from django.utils import timezone
from django.db.models import *
from django.urls import reverse
from account_app.models import TeacherProfile, StudentProfile

# Create your models here.


class Classroom(Model):
    teacher = ForeignKey(TeacherProfile, on_delete=CASCADE, default=1)
    students = ManyToManyField(StudentProfile)
    class_name = CharField(max_length=50)
    subject = CharField(max_length=50, default='Add The Subject You Will be Teaching')
    description = CharField(max_length=100, default='This is a Class')
    date_posted = DateTimeField(default=timezone.now)

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return reverse('classroom', kwargs={'pk': self.pk})

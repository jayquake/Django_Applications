from forum.models import Comment
from .models import Classroom
from account_app.models import StudentProfile
from django.forms import *


class CreateClassForm(ModelForm):
    class Meta:
        model = Classroom
        class_name = CharField(max_length=50)
        subject = CharField(max_length=50)
        fields = ('class_name', 'subject', 'description', 'students')


Students = (StudentProfile.objects.all())


class ClassUpdateForm(ModelForm):
    class Meta:
        model = Classroom
        students = SelectMultiple(choices=Students)
        fields = ('class_name', 'subject', 'description', students)


# class StudentCommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)
#

# class UpdateCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)

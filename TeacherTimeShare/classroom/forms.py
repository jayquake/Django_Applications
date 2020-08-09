from forum.models import Comment
from .models import Classroom
from account_app.models import StudentProfile
from django.forms import *
from django.forms import CheckboxSelectMultiple
from multiselectfield import *


class CreateClassForm(ModelForm):
    class Meta:
        model = Classroom
        class_name = CharField(max_length=50)
        subject = CharField(max_length=50)
        fields = ('class_name', 'subject', 'description', 'students')


Students = (StudentProfile.objects.all())


class ClassUpdateForm(ModelForm):
    class Meta:
        boost = {'class': 'form-control w-60'}
        fields = ('class_name', 'subject', 'description', 'students')
        model = Classroom
        widgets = {
            'class_name': TextInput({'class': 'form-control w-60'}),
            'subject': TextInput({'class': 'form-control w-60'}),
            'description': TextInput({'class': 'form-control w-60'}),
            'students': CheckboxSelectMultiple({'class': 'form-control ml-5 w-100 lead'}),
        }

# class StudentCommentForm(ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)
#

# class UpdateCommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)

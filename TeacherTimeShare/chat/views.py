from django.shortcuts import render, get_object_or_404

# Create your views here.
from account_app.models import User, StudentProfile
from classroom.models import Classroom


def index(request):
    user = Classroom.objects.filter(teacher_id=request.user.teacherprofile.pk)
    context = {
        'classes': user.all()
    }
    return render(request, 'chat/index.html', context)


def room(request, room_name):
    classroom = Classroom.objects.filter(teacher_id=request.user.teacherprofile.pk)
    class_student = StudentProfile.objects.all()


    context = {
        'classes': classroom.all(),
        'room_name': room_name,
        'user': request.user,
        'classroom': classroom,
        'class_student': class_student
    }
    return render(request, 'chat/room.html', context)

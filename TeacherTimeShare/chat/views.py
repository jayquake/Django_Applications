from django.shortcuts import render

# Create your views here.
from account_app.models import User
from classroom.models import Classroom


def index(request):
    user = Classroom.objects.filter(teacher_id=request.user.teacherprofile.pk)
    context = {
        'classes': user.all()
    }
    return render(request, 'chat/index.html', context)


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user': request.user,
    })

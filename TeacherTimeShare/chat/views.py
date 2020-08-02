from django.shortcuts import render

# Create your views here.
from account_app.models import User


def index(request):
    context ={
        'users': User.objects.all,

    }
    return render(request, 'chat/index.html', context)


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user': request.user,
    })

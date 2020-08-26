from django.shortcuts import render, get_object_or_404

# Create your views here.
from account_app.models import User, StudentProfile
from classroom.models import Classroom


def enter_class(request, pk):
    class_room_exact = get_object_or_404(Classroom, pk=pk)
    user = Classroom.objects.filter(teacher_id=request.user.teacherprofile.pk)
    context = {
        'classes': user.all(),
        'classroom': class_room_exact
    }
    return render(request, 'chat/enter_class.html', context)


def room(request, pk):
    class_room_exact = get_object_or_404(Classroom, pk=pk)
    student_user = User.objects.all()
    class_students_exact = StudentProfile.objects.all()

    context = {
        'class_room_exact': class_room_exact,
        'user': request.user,
        'student_user': student_user,
        'class_students_exact': class_students_exact,

    }
    return render(request, 'chat/room.html', context)

    # for stu in class_students_exact:
    #
    #     for stud in class_room_exact.students:
    #
    #         if stud.user_id in stu.user.id:
    #             student = stu.user.username

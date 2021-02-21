from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import CreateClassForm, ClassUpdateForm

from .models import Classroom
from account_app.models import StudentProfile


# Create your views here.


class ClassroomCreateView(LoginRequiredMixin, CreateView):
    model = Classroom
    fields = ['class_name', 'subject']

    def form_valid(self, form):
        class_info = Classroom(teacher_id=self.request.user.teacherprofile.pk)
        class_info.save(True)
        return super().form_valid(form)


class ClassroomListView(ListView):
    model = Classroom
    template_name = 'classroom/class_list.html'
    context_object_name = 'classes'
    ordering = ['-date_posted']
    paginate_by = 3


def classroom(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    my_students = classroom.students.all()
    all_students = classroom.students.all()
    ordering = ['-date_posted']
    paginate_by = 3
    context = {
        'class': classroom,
        'my_students': my_students,
        'all_students': all_students
    }

    return render(request, 'classroom/classroom.html', context)


def my_classes(request):
    user = Classroom.objects.filter(teacher_id=request.user.teacherprofile.pk)
    context = {
        'classes': user.all(),
    }
    return render(request, 'classroom/my_classes.html', context)


class ClassroomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Classroom
    form_class = ClassUpdateForm

    def form_valid(self, form):
        students = StudentProfile
        form.instance.teacher.user.pk = self.request.user.teacherprofile.pk
        return super().form_valid(form)

    def test_func(self):
        students = StudentProfile
        class_to_update = self.get_object()
        if self.request.user.id == class_to_update.teacher.user.id:
            return True
        return False


class ClassroomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Classroom
    success_url = '/classroom/my_classes'

    def test_func(self):
        class_to_update = self.get_object()
        if self.request.user.id == class_to_update.teacher.user.id:
            return True
        return False


def enroll(request, class_id):
    if request.method == 'GET':
        student = StudentProfile.objects.filter(user_id=request.user.studentprofile.user_id)
        classroom_exact = get_object_or_404(Classroom, id=class_id)
        classroom_exact.students.set(student)
        classroom_exact.save(True)

    context = {
        'classroom': classroom_exact,
    }

    return render(request, 'classroom/classroom_enroll.html', context)

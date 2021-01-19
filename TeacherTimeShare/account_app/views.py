from django.views.generic import CreateView, TemplateView
from .models import User, TeacherProfile, StudentProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TeacherUpdateFrom, TeacherProfileUpdateForm, StudentUpdateFrom, StudentProfileUpdateForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import StudentRegisterForm, TeacherRegisterForm
from .models import User
from classroom.models import Classroom
from forum.models import Post


class SignUpView(TemplateView):
    template_name = 'account_app/account_type.html.html'


def home(request):
    context = {
        'all_classes': Classroom.objects.all(),
        'all_posts': Post.objects.all()

    }

    return render(request, 'home.html', context)


def register(request):
    return render(request, 'account_app/account_type.html')


class StudentRegisterView(CreateView):
    model = User
    form_class = StudentRegisterForm
    template_name = 'account_app/register_student.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class TeacherRegisterView(CreateView):
    model = User
    form_class = TeacherRegisterForm
    template_name = 'account_app/register_teacher.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


@login_required
def profile(request):
    # CREATING TEACHER PROFILE
    if request.user.is_teacher:
        user_profile, created = TeacherProfile.objects.get_or_create(user=request.user)
        if request.method == 'GET':
            user_profile, created = TeacherProfile.objects.get_or_create(user=request.user)
        if request.method == "POST":
            teacher_update_form = TeacherUpdateFrom(request.POST, instance=request.user.teacherprofile)
            teacher_profile_form = TeacherProfileUpdateForm(request.POST, request.FILES,
                                                            instance=request.user.teacherprofile)
            if teacher_update_form.is_valid() or teacher_profile_form.is_valid():
                first = teacher_update_form.cleaned_data['first_name']
                last = teacher_update_form.cleaned_data['last_name']
                email = teacher_update_form.cleaned_data['email']

                request.user.first_name = first
                request.user.last_name = last
                request.user.email = email
                request.user.save()
                teacher_update_form.save()
                teacher_profile_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')
        else:
            teacher_update_form = TeacherUpdateFrom(instance=request.user.teacherprofile)
            teacher_profile_form = TeacherProfileUpdateForm(instance=request.user.teacherprofile)
        context = {
            'u_form': teacher_update_form,
            'p_form': teacher_profile_form,

        }
        return render(request, 'account_app/teacher_profile.html', context)
    # CREATING Student USERS
    elif request.user.is_student:
        if request.method == 'GET':
            user_profile, created = StudentProfile.objects.get_or_create(user=request.user)
        if request.method == "POST":
            student_update_form = StudentUpdateFrom(request.POST, instance=request.user.studentprofile)
            student_profile_form = StudentProfileUpdateForm(request.POST, request.FILES,
                                                            instance=request.user.studentprofile)
            if student_update_form.is_valid() or student_profile_form.is_valid():
                student_update_form.save()
                student_profile_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')
        else:
            student_update_form = StudentUpdateFrom(instance=request.user.studentprofile)
            student_profile_form = StudentProfileUpdateForm(instance=request.user.studentprofile)
        context = {
            'u_form': student_update_form,
            'p_form': student_profile_form,

        }
        return render(request, 'account_app/student_profile.html', context)
    return

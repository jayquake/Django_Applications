from django.urls import include, path
from .views import StudentRegisterView, TeacherRegisterView, SignUpView, home, register, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', StudentRegisterView.as_view(), name='register_student'),
    path('accounts/signup/teacher/', TeacherRegisterView.as_view(), name='register_teacher'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]

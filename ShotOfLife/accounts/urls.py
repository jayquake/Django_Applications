from django.urls import include, path
from .views import ContributorRegisterView, DownloaderRegisterView, registration_home,profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', registration_home, name='registration_home'),
    path('account/profile/', profile, name='profile'),
    path('accounts/signup/auth/contrib/', ContributorRegisterView.as_view(), name='register_contributor'),
    path('accounts/signup/auth/D/', DownloaderRegisterView.as_view(), name='register_downloader'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/registration/logout.html'), name='logout'),
]



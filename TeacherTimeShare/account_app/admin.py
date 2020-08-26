from django.contrib import admin

# Register your models here.
from account_app.models import User, StudentProfile, TeacherProfile, Profile

admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Profile)

from django.urls import path
from .views import ClassroomCreateView, classroom, ClassroomUpdateView, ClassroomDeleteView, my_classes, \
    ClassroomListView, enroll

urlpatterns = [
    path('', ClassroomListView.as_view(), name='class_list'),
    path('create/', ClassroomCreateView.as_view(), name='create_class'),
    path('classroom/<int:pk>/', classroom, name='classroom'),
    path('my_classes/', my_classes, name='my_classes'),
    path('class/<int:pk>/update/', ClassroomUpdateView.as_view(), name='class-update'),
    path('class/<int:pk>/delete/', ClassroomDeleteView.as_view(), name='class-delete'),
    path('class/enroll/<int:pk>/', enroll, name='classroom_enroll'),

]

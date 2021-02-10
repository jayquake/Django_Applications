from django.urls import include, path
from .views import photo_home_view, UploadView, post_detail, PostUpdateView, PostDeleteView, \
    comment_update_confirmation, comment_delete_confirmation, my_posts, post_upload
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', photo_home_view, name='photo_home_view'),
    path('my_porfolio/', my_posts, name='my-posts'),
    # path('post/new/', UploadView.as_view(), name='post-create'),
    path('post/new/', post_upload, name='post-create'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/update/ref_post/<int:post_id>/', comment_update_confirmation, name='comment-update'),
    path('comment/<int:pk>/delete/ref_post/<int:post_id>', comment_delete_confirmation, name='comment-delete'),

]

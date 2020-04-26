from django.urls import path
from .views import PostListView, post_detail, PostCreateView, PostUpdateView, PostDeleteView, my_posts, UserPostListView, comment_update_confirmation, comment_delete_confirmation
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='forum'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/update/ref_post/<int:post_id>/', comment_update_confirmation, name='comment-update'),
    path('comment/<int:pk>/delete/ref_post/<int:post_id>', comment_delete_confirmation, name='comment-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('user-posts/', my_posts, name='my-posts'),
]
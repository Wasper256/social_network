from django.urls import path

from .views import PostListCreateView, LikeView

app_name = 'posts'


urlpatterns = [
    path(r'posts/', PostListCreateView.as_view(), name='posts'),
    path(r'like_post/<int:post_id>/', LikeView.as_view(), name='like_posts'),
    ]

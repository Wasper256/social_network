from .views import PostListCreateView, LikeView
from django.urls import path, include
from apps.api.routers import router
app_name = 'posts'

# router.register(r'posts', PostListCreateView, base_name='post')

urlpatterns = [
    # path('posts/', include(router.urls)),
    path(r'posts/', PostListCreateView.as_view(), name='posts'),
    path(r'like_post/<int:post_id>/', LikeView.as_view(), name='like_posts'),
    ]

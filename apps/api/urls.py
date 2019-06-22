from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from apps.accounts import auth_views


app_name = 'api'

urlpatterns = [
    path('auth/registration/', auth_views.CustomRegisterView.as_view()),
    path('auth/login/', obtain_jwt_token),
    path('auth/api-token-refresh/', refresh_jwt_token),
    path('auth/', include('rest_auth.urls')),

    path('accounts/', include('apps.accounts.urls')),
    path('posts/', include('apps.posts.urls')),

]

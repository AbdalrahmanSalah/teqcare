from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreatUserView.as_view(), name='create'),
    path('api/token/', views.CustomTokenView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

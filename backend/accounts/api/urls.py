from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from .views import FollowUnfollowUserAPIView, MyTokenObtainPairView, UserDetailAPIView, SignupAPIView, ProfileUpdateAPIView


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("info/", UserDetailAPIView.as_view()),
    path("signup/", SignupAPIView.as_view()),
    path("profile/update/", ProfileUpdateAPIView.as_view()),
    path("follow/<int:pk>/", FollowUnfollowUserAPIView.as_view()),
    path('api/token/blacklist/', TokenBlacklistView.as_view(),
         name='token_blacklist'),
]

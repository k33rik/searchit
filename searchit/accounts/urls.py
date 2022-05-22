from django.urls import path

from accounts import views
from accounts.views import CustomLogoutView

urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('profile', views.profile, name='profile'),
    path('profile/change-password', views.CustomPasswordChangeView.as_view(), name='change-password'),
    path('logout', CustomLogoutView.as_view(), name='logout')
]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password', PasswordChangeView.as_view(), name='change-password'),
]

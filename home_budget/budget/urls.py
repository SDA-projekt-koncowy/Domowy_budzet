from django.urls import path

from budget import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
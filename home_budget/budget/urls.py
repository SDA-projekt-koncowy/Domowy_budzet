from django.urls import path

from budget import views


urlpatterns = [
    path('', views.index, name='index'),
]
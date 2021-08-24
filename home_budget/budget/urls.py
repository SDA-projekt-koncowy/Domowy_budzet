from django.urls import path

from budget import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('copyright/', views.copyright, name='copyright'),
    path('category/', views.CategoryView.as_view(), name='category')
]
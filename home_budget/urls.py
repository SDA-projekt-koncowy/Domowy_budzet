"""home_budget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from budget.views import IncomeCreateView, IncomeDeleteView, IncomeDetailView, IncomeListView, IncomeUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('income-list-view/', IncomeListView.as_view(), name="income-list-view"),
    path('income-create-view/', IncomeCreateView.as_view(), name="income-create-view"),
    path('income-update-view/<pk>/', IncomeUpdateView.as_view(), name="income-update-view"),
    path('income-delete-view/<pk>/', IncomeDeleteView.as_view(), name="income-delete-view"),
    path('income-detail-view/<pk>/', IncomeDetailView.as_view(), name="income-detail-view"),
    path('', include('budget.urls')),
]

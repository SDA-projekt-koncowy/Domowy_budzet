from django.urls import path

from budget import views



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('copyright/', views.copyright, name='copyright'),
    path('income-list-view/', views.IncomeListView.as_view(), name="income-list-view"),
    path('income-create-view/', views.IncomeCreateView.as_view(), name="income-create-view"),
    path('income-update-view/<pk>/', views.IncomeUpdateView.as_view(), name="income-update-view"),
    path('income-delete-view/<pk>/', views.IncomeDeleteView.as_view(), name="income-delete-view"),
    path('income-detail-view/<pk>/', views.IncomeDetailView.as_view(), name="income-detail-view")
]
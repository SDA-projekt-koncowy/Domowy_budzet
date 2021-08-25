from django.urls import path

from budget import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('copyright/', views.copyright, name='copyright'),
    path('expense-list-view/', views.ExpenseListView.as_view(), name="expense-list-view"),
    path('expense-create-view/', views.ExpenseCreateView.as_view(), name="expense-create-view"),
    path('expense-update-view/<pk>/', views.ExpenseUpdateView.as_view(), name="expense-update-view"),
    path('expense-delete-view/<pk>/', views.ExpenseDeleteView.as_view(), name="expense-delete-view"),
    path('expense-detail-view/<pk>/', views.ExpenseDetailView.as_view(), name="expense-detail-view"),
]
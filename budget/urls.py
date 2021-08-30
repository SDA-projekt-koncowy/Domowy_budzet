from django.urls import path

from budget import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('expense-list-view/', views.ExpenseListView.as_view(), name="expense-list-view"),
    path('expense-create-view/', views.ExpenseCreateView.as_view(), name="expense-create-view"),
    path('expense-update-view/<pk>/', views.ExpenseUpdateView.as_view(), name="expense-update-view"),
    path('expense-delete-view/<pk>/', views.ExpenseDeleteView.as_view(), name="expense-delete-view"),
    path('expense-detail-view/<pk>/', views.ExpenseDetailView.as_view(), name="expense-detail-view"),
    path('income-list-view/', views.IncomeListView.as_view(), name="income-list-view"),
    path('income-create-view/', views.IncomeCreateView.as_view(), name="income-create-view"),
    path('income-update-view/<pk>/', views.IncomeUpdateView.as_view(), name="income-update-view"),
    path('income-delete-view/<pk>/', views.IncomeDeleteView.as_view(), name="income-delete-view"),
    path('income-detail-view/<pk>/', views.IncomeDetailView.as_view(), name="income-detail-view"),
    path('copyright/', views.copyright, name='copyright'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('category-list-view/', views.CategoryListView.as_view(), name="category-list-view"),
    path('category-create-view/', views.CategoryCreateView.as_view(), name="category-create-view"),
    path('category-update-view/<pk>/', views.CategoryUpdateView.as_view(), name="category-update-view"),
    path('category-delete-view/<pk>/', views.CategoryDeleteView.as_view(), name="category-delete-view"),
    path('category-detail-view/<pk>/', views.CategoryDetailView.as_view(), name="category-detail-view"),
]

from django.contrib.auth.models import User
import django_filters
from budget.models import *

class UserFilterIncome(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['incomes__category']


class UserFilterExpense(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['expenses__category']


class IncomeFilter(django_filters.FilterSet):
    class Meta:
        model = Income
        fields = ['category']


class ExpenseFilter(django_filters.FilterSet):
    class Meta:
        model = Expense
        fields = ['category']


from django.shortcuts import render
from django.views.generic import ListView
from budget.models import Category, Income
# Create your views here.

class IncomeListView(ListView):
    template_name = "list.html"
    model = Income
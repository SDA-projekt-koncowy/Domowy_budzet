from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)
from budget.forms import IncomeForm
from budget.models import Income


# Create your views here.

class IncomeListView(ListView):
    template_name = "list.html"
    model = Income


class IncomeCreateView(CreateView):
    model = Income
    template_name = "form.html"
    success_url = reverse_lazy("income-list-view")
    form_class = IncomeForm


class IncomeUpdateView(UpdateView):
    model = Income
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("income-list-view")


class IncomeDeleteView(DeleteView):
    model = Income
    template_name = 'delete.html'
    success_url = reverse_lazy("income-list-view")


class IncomeDetailView(DetailView):
    model = Income
    template_name = "my_incomes.html"
    extra_context = {
        "update_url": "income-update-view",
        "delete_url": "income-delete-view"
    }
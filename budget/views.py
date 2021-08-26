from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)
from budget.forms import IncomeForm
from budget.models import Income
from budget.models import Expense


def copyright(request):
    return render(
        request,
        template_name="copyright.html"
    )


class IndexView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return render(
                request,
                template_name="register_page.html"
            )

        return render(
            request,
            template_name="index.html"
        )


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


class ExpenseListView(ListView):
    template_name = "list.html"
    model = Expense


class ExpenseCreateView(CreateView):
    model = Expense
    template_name = "form.html"
    success_url = reverse_lazy("expense-list-view")
    form_class = IncomeForm


class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("expense-list-view")


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'delete.html'
    success_url = reverse_lazy("expense-list-view")


class ExpenseDetailView(DetailView):
    model = Expense
    template_name = "my_expenses.html"
    extra_context = {
        "update_url": "income-update-view",
        "delete_url": "income-delete-view"
    }

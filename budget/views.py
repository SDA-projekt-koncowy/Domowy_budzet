from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
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
from budget.forms import CategoryForm, ExpenseForm, IncomeForm
from budget.models import Category, Expense, Income


def copyright(request):
    return render(
        request,
        template_name="copyright.html"
    )


class SettingsView(View):

    def get(self, request):
        return render(
            request,
            template_name="settings.html"
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


class IncomeListView(LoginRequiredMixin, ListView):
    template_name = "income_list.html"
    model = Income

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    template_name = "form.html"
    success_url = reverse_lazy("income-list-view")
    form_class = IncomeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    template_name = "form.html"
    success_url = reverse_lazy("income-list-view")
    form_class = IncomeForm

    def render_to_response(self, context, **response_kwargs):
        if self.request.user == context['income'].user:
            return super().render_to_response(context)
        else:
            return HttpResponse('404')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = 'delete.html'
    success_url = reverse_lazy("income-list-view")

    def render_to_response(self, context, **response_kwargs):
        if self.request.user == context['income'].user:
            return super().render_to_response(context)
        else:
            return HttpResponse('404')


class IncomeDetailView(LoginRequiredMixin, DetailView):
    model = Income
    template_name = "my_incomes.html"

    def render_to_response(self, context, **response_kwargs):
        if self.request.user == context['income'].user:
            return super().render_to_response(context)
        else:
            return HttpResponse('404')


class ExpenseListView(LoginRequiredMixin, ListView):
    template_name = "expense_list.html"
    model = Expense

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    template_name = "form.html"
    success_url = reverse_lazy("expense-list-view")
    form_class = ExpenseForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    template_name = "form.html"
    success_url = reverse_lazy("expense-list-view")
    form_class = ExpenseForm

    def render_to_response(self, context, **response_kwargs):
        if self.request.user == context['expense'].user:
            return super().render_to_response(context)
        else:
            return HttpResponse('404')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    template_name = 'delete.html'
    success_url = reverse_lazy("expense-list-view")

    def render_to_response(self, context, **response_kwargs):
        if self.request.user == context['expense'].user:
            return super().render_to_response(context)
        else:
            return HttpResponse('404')


class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expense
    template_name = "my_expenses.html"

    def render_to_response(self, context, **response_kwargs):
        if self.request.user == context['expense'].user:
            return super().render_to_response(context)
        else:
            return HttpResponse('404')


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = "category_list.html"
    model = Category

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "form.html"
    success_url = reverse_lazy("category-list-view")
    form_class = CategoryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = "form.html"
    success_url = reverse_lazy("category-list-view")
    form_class = CategoryForm

    def render_to_response(self, context, **response_kwargs):
        if self.request.user == context['category'].user:
            return super().render_to_response(context)
        else:
            return HttpResponse('404')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = reverse_lazy("category-list-view")

    def render_to_response(self, context, **response_kwargs):
        if self.request.user == context['category'].user:
            return super().render_to_response(context)
        else:
            return HttpResponse('404')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = "my_category.html"

    def render_to_response(self, context, **response_kwargs):
        if self.request.user == context['category'].user:
            return super().render_to_response(context)
        else:
            return HttpResponse('404')


class Summary(LoginRequiredMixin, View):

    def get(self, request):
        return render(
            request,
            template_name="summary.html"
        )
from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
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

User = get_user_model()


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
        return self.request.user.income_set.all()


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    template_name = "form.html"
    success_url = reverse_lazy("income-list-view")
    form_class = IncomeForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    template_name = "form.html"
    success_url = reverse_lazy("income-list-view")
    form_class = IncomeForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

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
        return self.request.user.expense_set.all()


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    template_name = "form.html"
    success_url = reverse_lazy("expense-list-view")
    form_class = ExpenseForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    template_name = "form.html"
    success_url = reverse_lazy("expense-list-view")
    form_class = ExpenseForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

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
        return self.request.user.category_set.all()


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = "form.html"
    success_url = reverse_lazy("category-list-view")
    form_class = CategoryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        return self.request.user.category_set.all()


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
        user = User.objects.get(pk=request.user.id)
        in_categories = Category.objects.all().filter(user=user, category='IN')
        ex_categories = Category.objects.all().filter(user=user, category='EX')

        total_income_value = Income.objects.filter(
            user=user,
        ).aggregate(
            amount_sum=(Sum('amount')
                        ))['amount_sum']

        total_expense_value = Expense.objects.filter(
            user=user,
        ).aggregate(
            amount_sum=(Sum('amount')
                        ))['amount_sum']

        account_balance = round((total_income_value - total_expense_value), 2)

        dates = [
                    datetime(
                        timezone.now().year,
                        timezone.now().month,
                        1,
                    ).date() - relativedelta(
                        months=i
                    ) for i in range(6)
                ][::-1]

        in_result = {}


        for category in in_categories:
            month_res = []
            for month in dates:
                monthly_amount = Income.objects.filter(
                    user=request.user,
                    category__name=category,
                    date__year=month.year,
                    date__month=month.month,
                ).aggregate(
                    amount_sum=Sum('amount'),
                )['amount_sum']
                if monthly_amount is None:
                    month_res.append(0)
                else:
                    month_res.append(round(monthly_amount, 2))
            month_sum = sum(month_res)
            month_res.append(month_sum)
            in_result[category] = month_res

        ex_result = {}

        for category in ex_categories:
            month_res = []
            for month in dates:
                monthly_amount = Expense.objects.filter(
                    user=request.user,
                    category__name=category,
                    date__year=month.year,
                    date__month=month.month,
                ).aggregate(
                    amount_sum=Sum('amount'),
                )['amount_sum']
                if monthly_amount is None:
                    month_res.append(0)
                else:
                    month_res.append(round(monthly_amount, 2))
            month_sum = sum(month_res)
            month_res.append(month_sum)
            ex_result[category] = month_res

        monthly_income = []

        for month in dates:
            income = Income.objects.all().filter(
                user=user,
                date__year=month.year,
                date__month=month.month
            ).aggregate(
                amount_sum=(Sum('amount'))
            )['amount_sum']
            if income is None:
                monthly_income.append(0)
            else:
                monthly_income.append(round(income, 2))
        monthly_sum_income = sum(monthly_income)

        monthly_expenses = []

        for month in dates:
            expense = Expense.objects.all().filter(
                user=user,
                date__year=month.year,
                date__month=month.month
            ).aggregate(
                amount_sum=(Sum('amount'))
            )['amount_sum']
            if expense is None:
                monthly_expenses.append(0)
            else:
                monthly_expenses.append(round(expense, 2))
        monthly_sum_expenses = sum(monthly_expenses)
        balance = []

        for i in range(len(monthly_income)):
            result = monthly_income[i] - monthly_expenses[i]
            balance.append(result)
        balance_sum = sum(balance)

        context = {
            'dates': dates,
            'in_categories': in_categories,
            'ex_categories': ex_categories,
            'monthly_income': monthly_income,
            'monthly_sum_income': monthly_sum_income,
            'monthly_expenses': monthly_expenses,
            'monthly_sum_expenses': monthly_sum_expenses,
            'in_result': in_result,
            'ex_result': ex_result,
            'balance': balance,
            'balance_sum': balance_sum,
            'account_balance': account_balance,

        }
        return render(
            request,
            template_name="summary.html",
            context=context,
        )

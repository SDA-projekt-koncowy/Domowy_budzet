from datetime import datetime
import pytz
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from budget.models import Category, Income
from budget.models import Expense

utc = pytz.UTC

def negative_value_validator(value):
    if value < 0:
        raise ValidationError("You can't have negative income")


class IncomeForm(LoginRequiredMixin, forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, validators=[negative_value_validator])
    description = forms.CharField(max_length=128, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all().filter(category="IN"))
    date = forms.DateField

    class Meta:
        model = Income
        fields = ("amount", "description", "category", "date")


class ExpenseForm(LoginRequiredMixin, forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, validators=[negative_value_validator])
    description = forms.CharField(max_length=128, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all().filter(category="EX"))
    date = forms.DateField

    class Meta:
        model = Expense
        fields = ("amount", "description", "category", "date")


class CategoryForm(LoginRequiredMixin, forms.ModelForm):
    name = forms.CharField(max_length=128, required=False)
    category = forms.ChoiceField

    class Meta:
        model = Category
        fields = ["name", "category"]

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
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = self.request.user.category_set.filter(category="IN")

    amount = forms.DecimalField(max_digits=10, decimal_places=2, validators=[negative_value_validator])
    description = forms.CharField(max_length=128, required=False)
    date = forms.DateField

    class Meta:
        model = Income
        fields = ("amount", "description", "category", "date")


class ExpenseForm(LoginRequiredMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = self.request.user.category_set.filter(category="EX")

    amount = forms.DecimalField(max_digits=10, decimal_places=2, validators=[negative_value_validator])
    description = forms.CharField(max_length=128, required=False)
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

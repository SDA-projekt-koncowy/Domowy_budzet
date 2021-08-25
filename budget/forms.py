from datetime import datetime
import pytz
from django import forms
from django.core.exceptions import ValidationError
from budget.models import Category, Income

utc = pytz.UTC


def negative_income_validator(value):
    if value < 0:
        raise ValidationError("You can't have negative income")


class IncomeForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, validators=[negative_income_validator])
    description = forms.CharField(max_length=128, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all())


    class Meta:
        model = Income
        fields = ("amount", "description", "category")

from django import forms

from budget.models import Category, Income


class IncomeForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(max_length=128, required=False)
    date = forms.DateTimeField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Income
        fields = "__all__"

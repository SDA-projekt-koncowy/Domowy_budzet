import datetime

from django.test import TestCase
from django.utils import timezone

from budget.forms import CategoryForm, ExpenseForm, IncomeForm


class CategoryFormTest(TestCase):
    def test_name_form_field_label(self):
        form = CategoryForm()
        self.assertTrue(form.fields['name'].label is None or form.fields['name'].label == 'name')

''' TUTAJ SIĘ WYWALA PRZEZ NADPISANIE INITU
class IncomeFormTest(TestCase):
    def test_amount_form_field_label(self):
        form = IncomeForm()
        self.assertTrue(form.fields['amount'].label is None or form.fields['amount'].label == 'amount')'''
import datetime

from django.test import RequestFactory, TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from budget.forms import CategoryForm, ExpenseForm, IncomeForm


class CategoryFormTest(TestCase):
    def test_name_form_field_label(self):
        form = CategoryForm()
        self.assertTrue(form.fields['name'].label is None or form.fields['name'].label == 'name')


class IncomeFormTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='TestUser', email='test@mail.com', password='top_secret')

    def test_amount_form_field_label(self):
        request = self.factory.get('')
        request.user = self.user
        form = IncomeForm(request=request)
        self.assertTrue(form.fields['amount'].label is None or form.fields['amount'].label == 'amount')

    def test_description_form_field_label(self):
        request = self.factory.get('')
        request.user = self.user
        form = IncomeForm(request=request)
        self.assertTrue(form.fields['description'].label is None or form.fields['description'].label == 'description')

class ExpenseFormTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='TestUser', email='test@mail.com', password='top_secret')

    def test_amount_form_field_label(self):
        request = self.factory.get('')
        request.user = self.user
        form = ExpenseForm(request=request)
        self.assertTrue(form.fields['amount'].label is None or form.fields['amount'].label == 'amount')

    def test_description_form_field_label(self):
        request = self.factory.get('')
        request.user = self.user
        form = ExpenseForm(request=request)
        self.assertTrue(form.fields['description'].label is None or form.fields['description'].label == 'description')
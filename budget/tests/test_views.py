from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from budget.models import Category, Expense, Income


class CategoryListViewTest(TestCase):
    def setUp(self) -> None:
        test_user = User.objects.create_user(username='testuser', password='hjod5342#2jh')
        test_user.save()

        self.category = Category.objects.create(name='Salary', category='IN')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('category-list-view'))
        self.assertRedirects(response, "/accounts/login/?next=/category-list-view/")

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.get(reverse('category-list-view'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.get(reverse('category-list-view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_list.html')


class ExpenseListViewTest(TestCase):
    def setUp(self) -> None:
        test_user = User.objects.create_user(username='testuser', password='hjod5342#2jh')
        test_user.save()

        self.expense = Expense.objects.create(amount=5000,
                                              description='whatever',
                                              category = Category.objects.create(
                                                  name='salary', category='IN'
                                              ))

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('expense-list-view'))
        self.assertRedirects(response, "/accounts/login/?next=/expense-list-view/")

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.get(reverse('expense-list-view'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.get(reverse('expense-list-view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'expense_list.html')


class IncomeListViewTest(TestCase):
    def setUp(self) -> None:
        test_user = User.objects.create_user(username='testuser', password='hjod5342#2jh')
        test_user.save()

        self.income = Income.objects.create(amount=5000,
                                              description='whatever',
                                              category = Category.objects.create(
                                                  name='salary', category='IN'
                                              ))

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('income-list-view'))
        self.assertRedirects(response, "/accounts/login/?next=/income-list-view/")

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.get(reverse('income-list-view'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.get(reverse('income-list-view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'income_list.html')
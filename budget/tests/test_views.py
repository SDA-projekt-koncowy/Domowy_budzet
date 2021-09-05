from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from budget.models import Category, Expense, Income


class IndexTest(TestCase):
    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class CopyrightTest(TestCase):
    def test_copyright(self):
        response = self.client.get(reverse('copyright'))
        self.assertEqual(response.status_code, 200)


class SettingsTest(TestCase):
    def test_settings(self):
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 200)


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
                                              category=Category.objects.create(
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
                                            category=Category.objects.create(
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


class CategoryCreateViewTest(TestCase):
    def test_create_category(self):
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.post(reverse('category-create-view'), {'name': 'salary', 'category': 'IN'})
        self.assertEqual(response.status_code, 302)


# sprawdzić czy faktycznie obiekt się tworzy, sprawdzić czy jeśli jest nie zalogowany,
# trzeba też sprawdzić co się stanie jak podamy puste dane
class IncomeCreateViewTest(TestCase):
    def test_create_expense(self):
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.post(reverse('income-create-view'),
                                    {'amount': 1000, 'description': 'whatever', 'category': 'EX'})
        self.assertEqual(response.status_code, 302)


# sprawdzić czy faktycznie obiekt się tworzy
class ExpenseCreateViewTest(TestCase):
    def test_create_income(self):
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.post(reverse('expense-create-view'),
                                    {'amount': 5000, 'description': 'whatever', 'category': 'IN'})
        self.assertEqual(response.status_code, 302)


class CategoryUpdateViewTest(TestCase):
    def test_update_category(self):
        category = Category.objects.create(name='Salary', category='IN')
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.post(reverse('category-update-view', kwargs={'pk': category.id}),
                                    {'name': 'salary', 'category': 'IN'})
        self.assertEqual(response.status_code, 302)


class ExpenseUpdateViewTest(TestCase):
    def test_create_expense(self):
        expense = Expense.objects.create(amount=3000,
                                         description='description',
                                         category=Category.objects.create(name='Food', category='EX'))
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.post(reverse('expense-update-view', kwargs={'pk': expense.id}),
                                    {'amount': '4000', 'description': 'whatever', 'category': 'EX'})
        self.assertEqual(response.status_code, 302)


class IncomeUpdateViewTest(TestCase):
    def test_create_income(self):
        income = Income.objects.create(amount=6000,
                                       description='description',
                                       category=Category.objects.create(name='salary', category='IN'))
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.post(reverse('income-update-view', kwargs={'pk': income.id}),
                                    {'amount': '4000', 'description': 'whatever', 'category': 'IN'})
        self.assertEqual(response.status_code, 302)


class CategoryDetailViewTest(TestCase):
    def test_detail_category(self):
        category = Category.objects.create(name='Salary', category='IN')
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.get(reverse('category-detail-view', kwargs={'pk': category.id}))
        self.assertEqual(response.status_code, 302)


class ExpenseDetailViewTest(TestCase):
    def test_detail_income(self):
        expense = Expense.objects.create(amount=6000,
                                         description='description',
                                         category=Category.objects.create(name='salary', category='IN'))
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.get(reverse('expense-detail-view', kwargs={'pk': expense.id}))
        self.assertEqual(response.status_code, 302)


class IncomeDetailViewTest(TestCase):
    def test_detail_income(self):
        income = Income.objects.create(amount=6000,
                                       description='description',
                                       category=Category.objects.create(name='salary', category='IN'))
        login = self.client.login(username='testuser', password='hjod5342#2jh')
        response = self.client.get(reverse('income-detail-view', kwargs={'pk': income.id}))
        self.assertEqual(response.status_code, 302)

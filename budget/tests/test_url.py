from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget import views


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, views.IndexView)

    def test_expense_list_view_url_resolves(self):
        url = reverse('expense-list-view')
        self.assertEquals(resolve(url).func.view_class, views.ExpenseListView)

    def test_expense_create_view_url_resolves(self):
        url = reverse('expense-create-view')
        self.assertEquals(resolve(url).func.view_class, views.ExpenseCreateView)

    def test_expense_update_view_url_resolves(self):
        url = reverse('expense-update-view', args=['some_pk'])
        self.assertEquals(resolve(url).func.view_class, views.ExpenseUpdateView)

    def test_expense_delete_view_url_resolves(self):
        url = reverse('expense-delete-view', args=['some_pk'])
        self.assertEquals(resolve(url).func.view_class, views.ExpenseDeleteView)

    def test_expense_detail_view_url_resolves(self):
        url = reverse('expense-detail-view', args=['some_pk'])
        self.assertEquals(resolve(url).func.view_class, views.ExpenseDetailView)

    def test_income_list_view_url_resolves(self):
        url = reverse('income-list-view')
        self.assertEquals(resolve(url).func.view_class, views.IncomeListView)

    def test_income_create_view_url_resolves(self):
        url = reverse('income-create-view')
        self.assertEquals(resolve(url).func.view_class, views.IncomeCreateView)

    def test_income_update_view_url_resolves(self):
        url = reverse('income-update-view', args=['some_pk'])
        self.assertEquals(resolve(url).func.view_class, views.IncomeUpdateView)

    def test_income_delete_view_url_resolves(self):
        url = reverse('income-delete-view', args=['some_pk'])
        self.assertEquals(resolve(url).func.view_class, views.IncomeDeleteView)

    def test_income_detail_view_url_resolves(self):
        url = reverse('income-detail-view', args=['some_pk'])
        self.assertEquals(resolve(url).func.view_class, views.IncomeDetailView)

    def test_copyright_url_resolves(self):
        url = reverse('copyright')
        self.assertEquals(resolve(url).func, views.copyright)

    def test_settings_url_resolves(self):
        url = reverse('settings')
        self.assertEquals(resolve(url).func.view_class, views.SettingsView)

    def test_category_list_view_url_resolves(self):
        url = reverse('category-list-view')
        self.assertEquals(resolve(url).func.view_class, views.CategoryListView)

    def test_category_create_view_url_resolves(self):
        url = reverse('category-create-view')
        self.assertEquals(resolve(url).func.view_class, views.CategoryCreateView)

    def test_category_update_view_url_resolves(self):
        url = reverse('category-update-view', args=['some_pk'])
        self.assertEquals(resolve(url).func.view_class, views.CategoryUpdateView)

    def test_category_delete_view_url_resolves(self):
        url = reverse('category-delete-view', args=['some_pk'])
        self.assertEquals(resolve(url).func.view_class, views.CategoryDeleteView)

    def test_category_detail_view_url_resolves(self):
        url = reverse('category-detail-view', args=['some_pk'])
        self.assertEquals(resolve(url).func.view_class, views.CategoryDetailView)
    '''
    def test_balance_url_resolves(self):
        url = reverse('balance')
        self.assertEquals(resolve(url).func.view_class, views.Balance)

    def test_balance_list_url_resolves(self):
        url = reverse('balance-list')
        self.assertEquals(resolve(url).func.view_class, views.BalanceList)

    def test_balance_mix_url_resolves(self):
        url = reverse('balance-mix')
        self.assertEquals(resolve(url).func.view_class, views.BalanceMix)
    '''
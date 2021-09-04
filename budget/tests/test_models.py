from django.test import TestCase

from budget.models import Category, Expense, Income


# DOPISAĆ TESTY NA FIELD CHOICE
class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="salary", category='EX')
        print('patrzę ile razy się wywołuje')

    def test_name_label(self):
        # category = Category.objects.get(id=1)
        self.category.name = 'coś innego'
        self.category.save()
        field_label = self.category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_object_name(self):
        self.assertEqual("salary", self.category.name)

    def test_name_max_length(self):
        max_length = self.category._meta.get_field('name').max_length
        self.assertEqual(max_length, 128)

    def test_object_name_is_simply_name(self):
        expected_object_name = f"{self.category.name}"
        self.assertEqual(str(self.category), expected_object_name)

    def test_category_label(self):
        field_label = self.category._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_category_max_length(self):
        max_length = self.category._meta.get_field('category').max_length
        self.assertEqual(max_length, 128)

    def test_user_label(self):
        field_label = self.category._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')


class ExpenseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.expense = Expense.objects.create(amount=1000,
                                             description='description',
                                             category=Category.objects.create(
                                                 name="food",
                                                 category="IN"
                                             ))

    def test_amount_label(self):
        field_label = self.expense._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_amount_max_digits(self):
        max_digits = self.expense._meta.get_field('amount').max_digits
        self.assertEqual(max_digits, 10)

    def test_amount_decimal_places(self):
        decimal_places = self.expense._meta.get_field('amount').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_description_label(self):
        field_label = self.expense._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        max_length = self.expense._meta.get_field('description').max_length
        self.assertEqual(max_length, 128)

    def test_category_label(self):
        field_label = self.expense._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_user_label(self):
        field_label = self.expense._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')


class IncomeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.income = Income.objects.create(amount=5000,
                                             description='description',
                                             category=Category.objects.create(
                                                 name="salary",
                                                 category="IN"
                                             ))

    def test_amount_label(self):
        field_label = self.income._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_amount_max_digits(self):
        max_digits = self.income._meta.get_field('amount').max_digits
        self.assertEqual(max_digits, 10)

    def test_amount_decimal_places(self):
        decimal_places = self.income._meta.get_field('amount').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_description_label(self):
        field_label = self.income._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        max_length = self.income._meta.get_field('description').max_length
        self.assertEqual(max_length, 128)

    def test_category_label(self):
        field_label = self.income._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_user_label(self):
        field_label = self.income._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')
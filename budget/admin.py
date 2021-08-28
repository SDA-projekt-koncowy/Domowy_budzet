from django.contrib import admin

# Register your models here.

from budget.models import Category, Expense, Income

admin.site.register(Income)
admin.site.register(Category)
admin.site.register(Expense)

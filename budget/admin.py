from django.contrib import admin

# Register your models here.

from budget.models import Category, Income, Expense

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Category)

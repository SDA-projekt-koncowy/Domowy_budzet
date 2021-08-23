from django.contrib import admin

# Register your models here.

from budget.models import Category, Income

admin.site.register(Income)
admin.site.register(Category)

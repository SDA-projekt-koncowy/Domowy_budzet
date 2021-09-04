from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    CHOICES = (
        ('IN', 'Income'),
        ('EX', 'Expense'),
    )
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=128, choices=CHOICES, null=True)

    def __str__(self):
        return f"{self.name}"


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=128)
    date = models.DateTimeField(default=timezone.localdate().strftime('%Y-%m-%d'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='expenses')

    def __str__(self):
        return f"{self.amount} - {self.category}"


class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=128)
    date = models.DateTimeField(default=timezone.localdate().strftime('%Y-%m-%d'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='incomes')

    def __str__(self):
        return f"{self.amount} - {self.category}"

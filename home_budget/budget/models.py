from django.db import models


# Create your models here.

class Income(models.Model):
    amount = models.IntegerField()
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Amount: {self.amount} - {self.description}"


class Category(models.Model):
    name = models.CharField(max_length=128)
    income = models.ForeignKey(Income, on_delete=models.CASCADE, related_name='categories', null=True, blank=True)

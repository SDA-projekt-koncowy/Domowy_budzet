from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')

from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class RegisterView(TemplateView):
    template_name = 'registration/register.html'


class LoginView(TemplateView):
    template_name = 'registration/login.html'


class HomeView(TemplateView):
    template_name = 'index.html'

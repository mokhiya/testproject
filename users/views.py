from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from users.forms import UserRegistrationForm
from users.models import UserModel


class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        print("Form is valid, attempting to save the user...")
        try:
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print(f"User saved successfully: {user.username}")
            return super().form_valid(form)
        except Exception as e:
            print(f"Error during user save: {e}")
            return self.form_invalid(form)

    def form_invalid(self, form):
        print(f"Form is invalid: {form.errors}")
        return super().form_invalid(form)


class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            user = None

        if user is not None:
            authenticated_user = authenticate(request, username=user.username, password=password)

            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, f'Welcome back, {authenticated_user.username}!')
                return redirect('/')
            else:
                messages.error(request, 'Invalid password.')
        else:
            messages.error(request, 'Invalid email address.')

        return self.get(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'index.html'

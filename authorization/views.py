import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from authorization.forms import RegisterForm, LoginForm
from authorization.services import save_user


class RegisterView(TemplateView):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                save_user(form)
                redirect_url = reverse_lazy('home')
                return redirect(redirect_url)
            except Exception as e:
                logging.error(e)
                messages.error(request, e, extra_tags='danger')
        return render(request, self.template_name, {'form': form})


class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        data = form.data
        username = data.get("username")
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        messages.error(request, "Bad credentials", extra_tags="danger")
        return render(request, self.template_name, {'form': form})
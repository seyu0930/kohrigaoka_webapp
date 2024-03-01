from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import list
from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignupForm



class LoginView(AuthLoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy('toppage:top')

login = LoginView.as_view()



class LogoutView(AuthLogoutView):
    template_name = "accounts/logout.html"
    success_url = reverse_lazy('toppage:top')

logout = LogoutView.as_view()



class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy('accounts:login')
    
signup = SignupView.as_view()
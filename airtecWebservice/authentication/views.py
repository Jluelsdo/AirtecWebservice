from django.shortcuts import render, reverse

from django.contrib.auth.views import LoginView, LogoutView

class LoginView(LoginView):
    template_name = 'authentication/login.html'
    
    def get_success_url(self):
        return reverse('home')

class LogoutView(LogoutView):
    template_name = 'authentication/logout.html'
    
    def get_success_url(self):
        return reverse('home')
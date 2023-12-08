"""Class based views for authentication app."""
# pylint: disable=E0102
from django.shortcuts import reverse

from django.contrib.auth.views import LoginView, LogoutView

class LoginView(LoginView):
    """Login view."""
    template_name = 'authentication/login.html'

    def get_success_url(self):
        """Redirect to homepage on successful login."""
        return reverse('home')

class LogoutView(LogoutView):
    """Logout view."""
    template_name = 'authentication/logout.html'

    def get_success_url(self):
        """Redirect to homepage on successful logout."""
        return reverse('home')

"""
Config for restapi app
"""
from django.apps import AppConfig

class RestapiConfig(AppConfig):
    """Config for restapi app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restapi'

# appUser/apps.py
from django.apps import AppConfig


class AppUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appUser'

    def ready(self):
        import appUser.signals
# appUser/apps.py
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppUserConfig(AppConfig):
    name = "appUser"
    verbose_name = _("appUser")
    default_auto_field = 'django.db.models.BigAutoField'
    

    def ready(self):
        import appUser.signals
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AppobjectstorageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "appObjectStorage"
    verbose_name = _("appObjectStorage")

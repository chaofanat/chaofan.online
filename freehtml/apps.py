from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class FreehtmlConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "freehtml"
    verbose_name = _("FreeHTML")

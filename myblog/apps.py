from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MyblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myblog'
    verbose_name = _('Myblog')

# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter()
def to_megabytes(size_in_bytes):
    megabytes = size_in_bytes / (1024 * 1024)
    return f"{megabytes:.2f}"

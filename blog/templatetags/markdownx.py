from django import template
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify


register = template.Library()


@register.filter()
def markdown(value, arg=None):
    if not value:
        return ''
    else:
        return mark_safe(markdownify(value))

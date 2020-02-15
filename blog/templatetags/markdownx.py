from django import template
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify


register = template.Library()


@register.filter()
def markdown(value, arg=None):
    if value:
        return mark_safe(markdownify(value))
    else:
        return ''

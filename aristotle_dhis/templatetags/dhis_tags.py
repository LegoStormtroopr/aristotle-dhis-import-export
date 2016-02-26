from django import template
register = template.Library()

@register.simple_tag
def public_flags(item):

    return "r-------"
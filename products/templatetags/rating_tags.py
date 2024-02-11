from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val

@register.filter
def diff(num, val):
    return num - val

# https://stackoverflow.com/questions/8494209/modulus-in-django-template

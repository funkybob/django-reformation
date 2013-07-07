
from django import template
from django.forms.util import flatatt

register = template.Library()

@register.tag
def attrs(attr_dict):
    '''
    Convert a dictionary of attributes to a single string.
    '''
    return flatatt(attr_dict)


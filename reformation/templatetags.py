"""
Django Reformation

(c) 2013  Curtis Maloney, Danielle Madeley

See LICENSE.
"""

from django.template import Library


register = Library()


@register.tag
def form(parser, token):
    """
    The {% form %} tag
    """

    pass


@register.tag
def field(parser, token):
    """
    The {% field %} tag
    """

    pass

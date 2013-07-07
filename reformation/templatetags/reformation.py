"""
Django Reformation

(c) 2013  Curtis Maloney, Danielle Madeley

See LICENSE.
"""

from django.template import Library, Node, Template, token_kwargs

from django.forms.util import flatatt

register = Library()


class FormNode(Node):
    """
    Node for the {% form %} tag
    """

    def __init__(self, form, nodelist, kwargs):

        self.form = form
        self.nodelist = nodelist
        self.kwargs = kwargs

    def render(self, context):

        form = self.form.resolve(context)
        content = self.nodelist.render(context)

        extra_context = {
            'tmpl': 'reformation/form.html',
            'content': content,
            'form': form,
        }
        extra_context.update(self.kwargs)

        context.update(extra_context)

        output = Template('''
            {% extends tmpl %}
            {% block form %}
            {{ content }}
            {% endblock form %}
        ''').render(context)

        context.pop()

        return output


@register.tag
def form(parser, token):
    """
    The {% form %} tag
    """

    bits = token.split_contents()[1:]

    form = parser.compile_filter(tokens.pop(0))
    kwargs = token_kwargs(tokens, parser)

    nodelist = parser.parse(('endform',))
    parser.delete_first_token()

    return FormNode(form, nodelist, kwargs)


@register.tag
def field(parser, token):
    """
    The {% field %} tag
    """

@register.tag
def attrs(attr_dict):
    '''
    Convert a dictionary of attributes to a single string.
    XXX Should we perform escaping?  Probably
    '''
    return flatatt(attr_dict)

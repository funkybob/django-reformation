"""
Django Reformation

(c) 2013  Curtis Maloney, Danielle Madeley

See LICENSE.
"""

from django.template import Library, Node, Template, Variable, token_kwargs
from django.forms.util import flatatt

from containers import defaultdict

register = Library()


class FormNode(Node):
    """
    Node for the {% form %} tag
    """

    def __init__(self, form, nodelist, kwargs):

        self.form = Variable(form)
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

    form = tokens.pop(0)
    kwargs = token_kwargs(tokens, parser)

    nodelist = parser.parse(('endform',))
    parser.delete_first_token()

    return FormNode(form, nodelist, kwargs)


@register.simple_tag
def field(field, **kwargs):
    extra_data = {
        'template': 'reformation/field.html',
        'field': field,
        'id': field.auto_id,
    }

    # Explode values from the BoundField
    for attr in ('value', 'errors', 'label', 'help_text', 'form', 'field',
        'id_for_label', 'name', 'html_name'):
        extra_data[attr] = getattr(field, attr)

    # Now merge in the supplied overrides
    extra_data.update(kwargs)

    tmpl = get_template(extra_data['template'])

    context.update(extra_data)
    result = tmpl.render(context)
    context.pop()

    return result


@register.tag
def attrs(attr_dict):
    '''
    Convert a dictionary of attributes to a single string.
    XXX Should we perform escaping?  Probably
    '''
    return flatatt(attr_dict)

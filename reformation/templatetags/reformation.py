"""
Django Reformation

(c) 2013  Curtis Maloney, Danielle Madeley

See LICENSE.
"""

from django.template import Library, Node, Template, Variable


register = Library()


class FormNode(Node):
    """
    Node for the {% form %} tag
    """

    def __init__(self, form, nodelist):

        self.form = Variable(form)
        self.nodelist = nodelist

    def render(self, context):

        form = self.form.resolve(context)
        content = self.nodelist.render(context)

        context.update(dict(
            tmpl='reformation/form.html',
            content=content,
            form=form,
        ))

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

    tokens = token.split_contents()[1:]

    # FIXME: handle kwargs
    form, = tokens

    nodelist = parser.parse(('endform',))
    parser.delete_first_token()

    return FormNode(form, nodelist)


@register.tag
def field(parser, token):
    """
    The {% field %} tag
    """


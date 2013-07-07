"""
"""

from django.template import Template, Context


class RenderTemplateMixin(object):
    """
    Implement self.render_template()
    """

    module_name = None

    def render_template(self, tmpl, **kwargs):
        """
        Utility to render a template.
        """

        t = Template('{{% load {module} %}}{tmpl}'.format(
            module=self.module_name,
            tmpl=tmpl))
        ctx = Context(kwargs)

        return t.render(ctx)

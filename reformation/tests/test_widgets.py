"""
"""

from django.test import TestCase

from util import RenderTemplateMixin

class TestRenderForm(TestCase, RenderTemplateMixin):

    module_name = 'reformation'

    def test_form_tag(self):
        rendered = self.render_template('{% form form %}',
                                        form=None)

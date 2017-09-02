# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
class HomePafeTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page(self):
        request = HttpRequest()
        response = home_page(request)


        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        

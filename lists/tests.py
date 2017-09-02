# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.
class HomePafeTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

        

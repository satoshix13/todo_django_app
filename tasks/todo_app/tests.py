from django.test import TestCase
from django.urls import resolve
from .views import home
from django.http import HttpRequest
from django.template.loader import render_to_string




class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home)


    def test_home_page_returns_correct_html(self):
        """Home page returns correct html"""

        # request = HttpRequest()
        # response = home(request)
        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<!DOCTYPE html>'))
        # self.assertIn('<title>home</title>', html)
        # self.assertTrue(html.endswith('</html>'))

        response = self.client.get('/')

        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>home</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'todo_app/home.html')

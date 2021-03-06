from django.urls import reverse, resolve
from django.test import TestCase
from shortener.views import home


class HomeTestCases(TestCase):
    """Test Home page
    """
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEquals(self.response.status_code, 200)
        
    def test_home_page_contains_link_to_create_short_url(self):
        create_short_url = reverse('create_short_url')
        self.assertContains(self.response, f'href="{create_short_url}"')
    
    def test_home_page_contains_link_to_open_short_url(self):
        open_short_url = reverse('open_short_url')
        self.assertContains(self.response, f'href="{open_short_url}"')
        
    def test_home_page_resolves_to_home_view_func(self):
        view = resolve('/')
        self.assertEqual(view.func, home)
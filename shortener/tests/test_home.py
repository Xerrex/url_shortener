from django.urls import reverse
from django.test import TestCase


class HomeTest(TestCase):
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
    
    def test_home_page_contains_link_to_view_short_url(self):
        view_short_url = reverse('view_short_url')
        self.assertContains(self.response, f'href="{view_short_url}"')
        

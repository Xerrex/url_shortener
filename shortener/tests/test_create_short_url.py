from django.test import TestCase
from django.urls import reverse


class CreateShortUlrTestCases(TestCase):
    """Test the Create short url 
    """
    
    def setUp(self):
        self.url = reverse('create_short_url')
    
    def test_create_short_page_status_code(self):
        """Test Create short url page status code
        """
        pass
    
    def test_create_short_url_page_resolves_to_create_short_url_view(self):
        """Test create short_url page resolves 
        to create short url view function
        """
        pass
    
    def test_create_short_url_page_contains_CSRF(self):
        """Test Page contains CSRF
        """
        pass
    
    def test_create_short_url_page_contains_form(self):
        """Test page contains a form
        """
        pass
    
    
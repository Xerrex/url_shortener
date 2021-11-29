from django.test import TestCase
from django.urls import reverse, resolve

from shortener.views import create_short_url
from shortener.forms import NewShortUrlForm
from shortener.models import ShortUrl


class CreateShortUlrTestCases(TestCase):
    """Test the Create short url 
    """
    
    def setUp(self):
        self.url = reverse('create_short_url')
        self.response = self.client.get(self.url)
    
    def test_create_short_page_status_code(self):
        """Test Create short url page status code
        """
        self.assertEquals(self.response.status_code, 200)
    
    def test_create_short_url_page_for_view_func(self):
        """Test resolves to create short url 
        view function
        """
        view = resolve('/short/create')
        self.assertEquals(view.func, create_short_url)
    
    def test_create_short_url_page_contains_CSRF(self):
        """Test contains CSRF token: create short_url
        """
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_create_short_url_page_contains_form(self):
        """Test contains a form: create short_url 
        """
        form = self.response.context.get('form')
        self.assertEquals(form, NewShortUrlForm)
    
    def test_create_short_url_with_valid_data_post_data(self):
        """Test with valid data: create short url
        """
        data = {"original_url": "http://localhost:8000/"}
        
        response = self.client.post(self.url, data)
        self.assertTrue(ShortUrl.objects.exists())
    
    def test_create_short_url_with_invalid_post_data(self):
        """Test with invalid data: create short url
        """
        response = self.client.post(self.url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
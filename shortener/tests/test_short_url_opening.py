from django.http import response
from django.test import TestCase
from django.urls import reverse, resolve

from shortener.models import ShortUrl
from shortener.views import open_short_url


class OpenShortUrlTestCase(TestCase):
    """Test Cases for the Opening 
    Short url to view details
    """
    def setUp(self):
        self.url = reverse('open_short_url')
        self.response = self.client.get(self.url)
        
        create_url = reverse('create_short_url')
        data = {"original_url": "http://localhost:8000/"}
        self.client.post(create_url, data)
    
    def test_resolves_open_short_view_func(self):
        """Test resolves to open_short view finction
        """
        view = resolve(self.url)
        self.assertEquals(view.func, open_short_url)
    
    def test_contains_form(self):
        """Test contains form: open short url
        """
        self.assertContains(self.response, 'form')
    
    def test_contains_CSRF(self):
        """Test page contains CSRF token: open short url
        """
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_opening_short_urls(self):
        """Test opening a short urls: Open short url
        """
        shorturl = ShortUrl.objects.all()[0]
        data = {"short_url": shorturl.short_url}
        
        response = self.client.post(self.url, data)
        self.assertRedirects(response, f'/short/{data["short_url"]}')
    
    def test_opening_not_existing_short_url(self):
        """Test the opening of none existing url: open short url
        """
        data = {"short_url": "1234563"}
        response = self.client.post(self.url, data)
        
        self.assertContains(response, data["short_url"])
        
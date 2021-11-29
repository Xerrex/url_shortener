from django.test import TestCase
from django.urls import resolve, reverse

from shortener.models import ShortUrl
from shortener.views import view_short_url


class ViewshortUrlDetailsTestCases(TestCase):
    """Tests for the viewing short url details
    """
    def setUp(self):
        # create short Url
        data = {"original_url": "http://localhost:8000/"}
        self.client.post(reverse('create_short_url'), data)
        
        # create the view short url
        self.shorturl = ShortUrl.objects.all()[0]
        self.url = reverse("view_short_url", kwargs={"shortURL":self.shorturl.short_url})
        self.response = self.client.get(self.url)
    
    def test_page_status_code(self):
        """Test the page status code: view short url details
        """
        self.assertTrue(ShortUrl.objects.exists())
        self.assertEquals(self.response.status_code, 200)
    
    def test_resolves_to_view_short_url_func(self):
        """Test page Resolves to view_short_url
        """
        view = resolve(self.url)
        self.assertEquals(view.func, view_short_url)
        
    def test_page_contains_table(self):
        """Test page contains table to show url details
        """
        self.assertContains(self.response, '<table')
        self.assertContains(self.response, self.shorturl.short_url)
    
    def test_short_url_detail_accuracy(self):
        """Test the accuracy of the data showed by page
        """
        context_shorturl = self.response.context.get("shortUrl")
        self.assertIsInstance(context_shorturl, ShortUrl)
        self.assertEquals(context_shorturl.short_url, self.shorturl.short_url)
        self.assertEquals(context_shorturl.expiry_date, self.shorturl.expiry_date)
    
    def test_page_contains_redirect_link(self):
        """Test page contains link to redirect to original url
        """
        redirect_url = reverse('redirect_short_url', kwargs={'shortURL':self.shorturl.short_url})
        self.assertContains(self.response, f'href="{redirect_url}"')
    
    
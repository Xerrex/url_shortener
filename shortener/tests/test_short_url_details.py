from django.test import TestCase
from django.urls import resolve, reverse

from shortener.models import ShortUrl
from shortener.views import view_short_url, redirect_to_url


class ViewshortUrlDetailsTestCases(TestCase):
    """Tests for the viewing short url details
    """
    def setUp(self):
        # create short Url
        data = {"original_url": "http://localhost:8000/"}
        self.client.post(reverse('create_short_url'), data)
        
        # create the view short url
        self.shorturl = ShortUrl.objects.all()[0]
        
        kwargs={"shortURL":self.shorturl.short_url}
        self.url = reverse("view_short_url", kwargs=kwargs)
        self.redirect_url = reverse('redirect_short_url', kwargs=kwargs)
        
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
        self.assertContains(self.response, f'href="{self.redirect_url}"')

    def test_updating_times_visited_in_short_url_objects(self):
        """Test that redirecting to orginal url 
        changes times visited
        """
        self.assertEquals(self.shorturl.times_visited, 0)
        
        self.client.get(self.redirect_url)
        shorturl = ShortUrl.objects.all()[0]
        self.assertEquals(shorturl.times_visited, 1)
    
    def test_redirecting_to_original_url_resolves_to_redirect_to_url_func(self):
        """Test redirecting to original url resolves 
        to redirect_to_url func
        """
        view = resolve(self.redirect_url)
        self.assertEquals(view.func, redirect_to_url)

    def test_redirecting_to_correct_url(self):
        """Test that opening the redirect url opens
        the original url of the short urls
        """
        response = self.client.get(self.redirect_url)
        self.assertEquals(response.url, self.shorturl.original_url)
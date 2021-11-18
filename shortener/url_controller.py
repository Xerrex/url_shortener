from .models import ShortUrl
from .utils import generate_short_url

def create_shortUrl(original_url):
    """Create short url anda save to db

    Args:
        original_url (URL): The full url
    """
    shorturl = ShortUrl.objects.create(
        original_url=original_url,
        short_url = generate_short_url(10)
    )
    
    return shorturl
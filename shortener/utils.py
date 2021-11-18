from random import choice
from string import ascii_letters, digits
from django.utils import timezone


def default_expiry_time():
    """Defines the expiry time
    
    Creates a default timezone 
    object that is 5 days from today
    """
    return timezone.now() + timezone.timedelta(days=5)


def generate_short_url(size):
    """Creates a shortened url
    
    It chooses randomly from a 
    combination of a-z and 0-9
    """
    
    choose_from = ascii_letters + digits
    short_url = "".join(
        [choice(choose_from) for _ in range(size+1)]
    )
    
    return short_url
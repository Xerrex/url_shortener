from django.utils import timezone


def default_expiry_time():
    """Defines the expiry time
    
    Creates a default timezone 
    object that is 5 days from today
    """
    return timezone.now() + timezone.timedelta(days=5)

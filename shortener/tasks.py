from celery import shared_task
from django.utils import timezone
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def test_task():
    logger.info("First task in the url_shortener")


@shared_task
def delete_expired_shortened_urls():
    from .models import ShortUrl
    today = timezone.now()
    
    expired_urls = ShortUrl.objects.filter(expired_date__lt=today)
    msg =  expired_urls.delete()
    # msg ="Tuko hapa sasa"
    logger.info(f"Deleting expired URLS: {msg}")
    
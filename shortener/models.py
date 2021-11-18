from django.db import models
from .utils import default_expiry_time


class ShortUrl(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(default=default_expiry_time)
    times_visited = models.PositiveIntegerField(default=0)

        
    def __str__(self) -> str:
        return f"ShortUrl - {self.short_url} - {self.expiry_date}"
    
    
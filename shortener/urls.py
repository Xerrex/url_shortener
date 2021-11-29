from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('short/create', views.create_short_url, name="create_short_url"), # create a short
    path('short/open', views.open_short_url, name="open_short_url"), # page to open short url
    
    path('short/<str:shortURL>', views.view_short_url, name="view_short_url"), # short url page pJ0cMrAlqqw
    path('short/<str:shortURL>/redirect', views.redirect_to_url, name="redirect_short_url"),
]

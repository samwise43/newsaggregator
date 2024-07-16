from django.urls import path
from news.views import scraper, news_list
urlpatterns = [
  path('scraper/', scraper, name="scraper"),
  path('', news_list, name="home"),
]
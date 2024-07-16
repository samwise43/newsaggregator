from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as bsoup
from news.models import Headlines
# Create your views here.


def scraper(request):
    doc = requests.get("https://www.theonion.com/breaking-news/news").text

    soup = bsoup(doc, 'html.parser')
    news = soup.find_all('article')

    for article in news:
        link = article.find_all('a', {'class':'sc-1out364-0 dPMosf js_link'})[0]['href']
        title = article.find('h2').string
        image = article.find('source')['data-srcset']

        new_headline = Headlines()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image
        new_headline.save()
    return redirect("../")
        
def news_list(request):
    headlines = Headlines.objects.all()
    context = {
        'object_list': headlines,
    }
    return render(request, "news/home.html", context)
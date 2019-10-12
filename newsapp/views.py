from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here. 
# API Key : 52af66723d7a4b10b0086de9d5f1ff54

def index(request):

    newsapi = NewsApiClient(api_key = '52af66723d7a4b10b0086de9d5f1ff54')
    top = newsapi.get_top_headlines(sources = 'bbc-news')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    myList = zip(news, desc, img)

    return render(request, 'index.html', context = {"mylist": myList})

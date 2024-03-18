from django.shortcuts import render
from events.models import EventModel
from news.models import NewsModel
from articles.models import ArticleModel
from users.models import UserModel


def home_view(request):
    events = EventModel.objects.filter(status="published")[::-1][:6:]
    news = NewsModel.objects.filter(status="published")[::-1][:6:]
    articles = ArticleModel.objects.filter(status="published")[::-1][:6:]
    staffs = UserModel.objects.all()

    context = {
        "events": events,
        "news": news,
        "articles": articles,
        "staffs": staffs,
    }

    return render(request, "home/home.html", context)

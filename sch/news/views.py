from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import NewsModel


def news_view(request):
    news = NewsModel.objects.filter(status="published")[::-1]

    try:
        page_num = request.GET.get("pn", 1)
    except:
        page_num = 1

    paginator = Paginator(news, 2)
    paginated_objects = paginator.get_page(page_num) # paginated

    context = {
        "paginated_objects": paginated_objects,
    }

    # context = {
    #     "news": news,
    # }

    return render(request, "news/news.html", context)


def news_page_view(request, slug):
    news_page = get_object_or_404(NewsModel, slug=slug)

    context = {
        "news_page": news_page,
    }

    return render(request, "news/news-page.html", context)

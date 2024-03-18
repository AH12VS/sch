from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import ArticleModel, ArticleCommentModel
from .forms import ArticleCommentForm
from taggit.models import Tag
from django.utils import timezone
from datetime import datetime

DATETIME_FORMAT_FOR_SESSIONS = "%Y-%m-%d %H:%M:%S"


def articles_view(request, tag_slug=None):
    articles = ArticleModel.objects.filter(status="published")

    tag = None
    if tag_slug:
        tag = Tag.objects.get(slug=tag_slug)
        articles = articles.filter(tags__in=[tag])

    articles = articles[::-1]

    try:
        page_num = request.GET.get("pn", 1)
    except:
        page_num = 1

    paginator = Paginator(articles, 2)
    paginated_objects = paginator.get_page(page_num)  # paginated
    # paginated_articles = paginator.get_page(page_num) # paginated

    context = {
        "paginated_objects": paginated_objects,
    }

    return render(request, "articles/articles.html", context)


def article_view(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    comments = article.article_comments.filter(
        is_active=True).order_by("-created")

    if f"view_session_check-{article.id}" not in request.session:
        request.session[f"view_session_check-{article.id}"] = str(
            (timezone.now()).strftime(DATETIME_FORMAT_FOR_SESSIONS))
        article.views_count += 1
        article.save()
    else:
        session = request.session[f"view_session_check-{article.id}"]
        session_time = datetime.strptime(session, DATETIME_FORMAT_FOR_SESSIONS)
        current_time = datetime.strptime((timezone.now()).strftime(
            DATETIME_FORMAT_FOR_SESSIONS), DATETIME_FORMAT_FOR_SESSIONS)

        if ((current_time - session_time).total_seconds()) > 1200:
            del request.session[f"view_session_check-{article.id}"]

    if request.method == "POST":
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            comment = ArticleCommentModel()
            cd = form.cleaned_data
            comment.article = article
            comment.name = cd["name"]
            comment.comment_msg = cd["comment_msg"]

            comment.save()

            return redirect("articles:article_page", slug)

    context = {
        "article": article,
        "comments": comments
    }

    return render(request, "articles/article.html", context)

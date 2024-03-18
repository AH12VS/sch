from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import EventModel


def events_view(request):
    events = EventModel.objects.filter(status="published")[::-1]

    try:
        page_num = request.GET.get("pn", 1)
    except:
        page_num = 1

    paginator = Paginator(events, 2)
    paginated_objects = paginator.get_page(page_num) # paginated

    context = {
        "paginated_objects": paginated_objects,
    }

    # context = {
    #     "events": events,
    # }

    return render(request, "events/events.html", context)


def event_view(request, slug):
    event = get_object_or_404(EventModel, slug=slug)

    context = {
        "event": event,
    }

    return render(request, "events/event.html", context)

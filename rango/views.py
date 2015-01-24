from django.template import RequestContext
from django.shortcuts import render_to_response
from rango import models


def generate_url(id_, value):
    """Generates an url by combining id of object and some string value."""
    return "%s_%s" % (id_, value.replace(' ', '_'))


def get_id_from_url(url):
    """Get id from url in the format 42_Some_text."""
    try:
        id_ = int(url.split('_')[0])
    except ValueError:
        id_ = None
    return id_


def index(request):
    context = RequestContext(request)
    categories = models.Category.objects.order_by('-likes')[:5]
    for category in categories:
        category.url = generate_url(category.id, category.name)
    pages = models.Page.objects.order_by('-views')[:5]
    context_dict = {'categories': categories, 'pages': pages}
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return render_to_response('rango/about.html')


def category(request, category_name_url):
    context = RequestContext(request)
    category_id = get_id_from_url(category_name_url)
    try:
        category = models.Category.objects.get(id=category_id)
        pages = models.Page.objects.filter(category=category)
        context_dict = {'category': category, 'pages': pages}
    except models.Category.DoesNotExist:
        context_dict = {'category_name_url': category_name_url}

    return render_to_response('rango/category.html', context_dict, context)

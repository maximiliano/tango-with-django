from django.template import RequestContext
from django.shortcuts import render_to_response
from rango import models


def index(request):
    context = RequestContext(request)
    categories = models.Category.objects.order_by('-likes')[:5]
    for category in categories:
        category.url = category.name.replace(' ', '_')
    context_dict = {'categories': categories}
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return render_to_response('rango/about.html')


def category(request, category_name_url):
    context = RequestContext(request)
    # category = models.Category.
    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name': category_name}
    try:
        category = models.Category.objects.get(name=category_name)
        pages = models.Page.objects.filter(category=category)
        context_dict['category'] = category
        context_dict['pages'] = pages
    except models.Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)

from django.template import RequestContext
from django.shortcuts import render_to_response
from rango import models


def index(request):
    context = RequestContext(request)
    categories = models.Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': categories}
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return render_to_response('rango/about.html')

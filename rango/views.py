from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)
    context_dict = {'bold_message': 'I am bold font from the context.'}
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return render_to_response('rango/about.html')

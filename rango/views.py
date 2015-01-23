from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World from rango app.')

def about(request):
    return HttpResponse('Rango says: Here is the about page.')

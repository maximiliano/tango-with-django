from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World from rango app. Go to <a href="/rango/about">about page</a>')

def about(request):
    return HttpResponse('Rango says: Here is the about page. Go to <a href="/rango/">main page</a>')

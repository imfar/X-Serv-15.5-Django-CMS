from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Recurso
from django.views.decorators.csrf import csrf_exempt


def root_page(request):

    recursos = Recurso.objects.all()
    lista = "<ul>"
    for my_rec in recursos:
        lista += '<li><a href="/' + my_rec.name + ' \
        ">' + my_rec.name + '</a></li>'
    lista += "</ul>"

    rpta = "<html><head><title>SARO-15.5-cms</title></head> \
            <body><h1>PAGINA PRINCIPL</h1>\
            <p>Los recursos hasta el momento son: \
            </p>" + lista + "</body></html>"
    return HttpResponse(rpta)


@csrf_exempt
def a_page(request, rec_name):
    try:
        recurso = Recurso.objects.get(name=rec_name)
        return HttpResponse(recurso.contenido)
    except Recurso.DoesNotExist:
        return HttpResponse("ERROR 404 NOT FOUND")

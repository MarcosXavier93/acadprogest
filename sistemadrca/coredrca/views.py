from django.shortcuts import render
from django.http.response import HttpResponse
from django.template  import RequestContext,loader 
# Create your views here.
def artigo(request,ano):
    return HttpResponse('Ola Mundo.Esse eh o ano '+ ano)

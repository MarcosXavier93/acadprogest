# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader
from coredrca.models import Aluno_GO
from coredrca.models import Aluno_DT
from coredrca.models import Aluno_IEP
from coredrca.models import Aluno_NR_10
from coredrca.models import Disciplina
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import get_user
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
def disciplinas(request):
    disciplinas=Disciplina.objects.all()
    template = loader.get_template('disciplinas.html')
    context = RequestContext(request,{'disciplinas':disciplinas})
    return HttpResponse(template.render(context))

def alunos(request):
    alunos_go = Aluno_GO.objects.all()
    current_user = request.user
    template = loader.get_template('alunos.html')
    context = RequestContext(request,{'alunos_go':alunos_go ,'id': current_user.id})
    return HttpResponse(template.render(context))
def sobre(request):
    template = loader.get_template('sobre.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
def aluno_iep(request):
    template = loader.get_template('aluno_iep.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
def aluno_dt(request):
    template = loader.get_template('aluno_dt.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
def aluno_nr_10(request):
    template = loader.get_template('aluno_nr_10.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
def departamentos(request):
    template = loader.get_template('departamentos.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
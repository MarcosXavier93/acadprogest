from django.conf.urls import url
from coredrca import views

urlpatterns = [
    url(r'^$', views.home),  
    url(r'^alunos$', views.alunos),       
    url(r'^sobre$', views.sobre),    
    url(r'^aluno_dt$', views.aluno_dt),  
    url(r'^aluno_iep$', views.aluno_iep),  
    url(r'^aluno_nr_10$', views.aluno_nr_10),  
    url(r'^disciplinas$', views.disciplinas),  
    url(r'^departamentos$', views.departamentos),  
]
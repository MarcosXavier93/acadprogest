from django.db import models
#from reportlab.lib.colors import black

# Create your models here.

class Credito(models.Model):
    d_credito = models.IntegerField()
    d_credito_p = models.IntegerField()
    a_credito_o = models.IntegerField()
    a_credito_l = models.IntegerField()

    #LEMBRAR DE COMENTAR DO ERRO QUE ESTAVA DANDO AQUI COM RETORNO DO STRING.
    def __str__(self):
        return unicode(self.d_credito)

class Departamento(models.Model):
    nome = models.CharField(max_length=300)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=300)
    departamento = models.ForeignKey(Departamento, null=True)

    def __str__(self):
        return self.nome

class Secretaria(models.Model):
    nome = models.CharField(max_length=300)
    tipo = models.IntegerField() #tipo 0 graduacaoo tipo 1 pos-graduacao
    departamento = models.ForeignKey(Departamento, null=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome =  models.CharField(max_length=300)
    secretaria = models.ForeignKey(Secretaria, null=True)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length = 300)
    codigo = models.CharField(max_length = 300)
    obr_let = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    credito = models.ForeignKey(Credito)
    d_requisito = models.ManyToManyField('Disciplina',blank=True )
    curso = models.ForeignKey(Curso)
    professor = models.ForeignKey(Professor, null=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=300)
    matricula = models.IntegerField()
    curso = models.ForeignKey(Curso)
    credito = models.ForeignKey(Credito)
    disciplinas = models.ManyToManyField(Disciplina, blank=True,null = True)

    def __str__(self):
        return self.nome

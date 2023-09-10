from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(req, nom, com):

    cur = Curso(nombre = nom, comision = com)
    cur.objects.save()

    return HttpResponse(f"""<p>curso: {cur.nombre}, de la comision {cur.comision} grabado correctamente</p>""")

def cursos(req):

    lista = Curso.objects.all()

    return render(req, "C1.html", {"listaC": lista})


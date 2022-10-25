from django.shortcuts import render
from .models import Project     #si veo el mapa extendido de MVT view interactua con models. Es para poder utilizar los modelos desde las vistas

# Create your views here.
def portfolio(request):
    projects = Project.objects.all()    #creo la lista proyectos que hace referencia a la clase Project donde tengo definido mi modelo Project
    return render(request, "portfolio/portfolio.html", {'projects': projects})  #agrego projects al return. Inyecto la lista de proyectos en el temlate en forma de diccionario
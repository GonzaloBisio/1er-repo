#  

from django.shortcuts import render

from .models import *

# Create your views here.

def home_views(request):
    alumnos = Alumno.objects.all()
    return render(request,"home.html",{"alumnos":alumnos})

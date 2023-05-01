from django.shortcuts import render
from django.http import HttpResponse
from .forms import AlumnosForm, MaestrosForm, AdministracionForm
from .models import Alumnos, Maestros, Administracion

def home(request):
    return render(request, 'home.html')

def alumnos(request):
    form = AlumnosForm()
    if request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            form.save()
    alumnos = Alumnos.objects.all()
    context = {'form': form, 'alumnos': alumnos}
    return render(request, 'alumnos.html', context)

def maestros(request):
    form = MaestrosForm()
    if request.method == 'POST':
        form = MaestrosForm(request.POST)
        if form.is_valid

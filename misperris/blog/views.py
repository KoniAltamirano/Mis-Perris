from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Usuario, Mascotas , Ciudad
from .forms import UsuarioForm
from .forms import MascotasForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from . import forms
from django.http import HttpResponse


# Create your views here.
def home(request):
    mascotas = Mascotas.objects.all().order_by()
    return render(request, 'blog/Main.html', {'mascotas':mascotas })

@login_required(login_url="/accounts/login/")
def registro(request):
    form = UsuarioForm()
    return render(request, 'blog/Registro.html', {'form': form})

@login_required(login_url="/accounts/login/")
def usuario_list(request):
    usuarios = Usuario.objects.filter().order_by('fecha_publicacion')
    return render(request, 'blog/Usuario_List.html', {'usuarios': usuarios})


@login_required(login_url="/accounts/login/")
def usuario_new(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.rut = request.user
            usuario.fecha_publicacion = timezone.now()
            usuario.save()
            return redirect('Usuario_Detail', pk=usuario.pk)
    else:
        form = UsuarioForm()
    return render(request, 'blog/Usuario_Edit.html', {'form': form})



@login_required(login_url="/accounts/login/")
def usuario_detail(request,pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'blog/Usuario_Detail.html', {'usuario': usuario})

def load_ciudades(request):
    region_id = request.GET.get('region')
    ciudades = Ciudad.objects.filter(region_id=region_id).order_by('nombre')
    return render(request, 'blog/ciudad_dropdown_list_options.html', {'ciudades': ciudades})

def mascota_list(request):
    mascotas = Mascotas.objects.filter().order_by('fecha_publicacion')
    return render(request, 'blog/mascota_list.html', {'mascotas':mascotas})

def mascota_detail(request, pk):
    mascotas = get_object_or_404(Mascotas, pk=pk)
    return render(request, 'blog/mascota_detail.html', {'mascotas': mascotas})

def mascota_new(request):
    form = MascotasForm()
    return render(request, 'blog/mascota_edit.html', {'form': form})

def mascota_new(request):
    if request.method == "POST":
        form = MascotasForm(request.POST)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.nombre = mascota.nombre
            mascota.fecha_publicacion = timezone.now()
            mascota.save()
            return redirect('blog:mascota_detail', pk=mascota.pk)
    else:
        form = MascotasForm()
    return render(request, 'blog/mascota_edit.html', {'form': form})

@login_required(login_url="/accounts/login/")
def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.rut = request.user
            usuario.save()
            return redirect('Usuario_Detail', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'blog/Usuario_Edit.html', {'form': form})


def mascota_edit(request, pk):
    mascota = get_object_or_404(Mascotas, pk=pk)
    if request.method == "POST":
        form = MascotasForm(request.POST, instance=mascota)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.author = request.user
            mascota.save()
            return redirect('blog:mascota_detail', pk=mascota.pk)
    else:
        form = MascotasForm(instance=mascota)
    return render(request, 'blog/mascota_edit.html', {'form': form})









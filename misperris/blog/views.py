from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Usuario
from .forms import UsuarioForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'blog/Main.html')

def registro(request):
    form = UsuarioForm()
    return render(request, 'blog/Registro.html', {'form': form})

@login_required(login_url="/accounts/login/")
def usuario_list(request):
    usuarios = Usuario.objects.filter().order_by('fecha_publicacion')
    return render(request, 'blog/Usuario_List.html', {'usuarios': usuarios})
@login_required(login_url="/accounts/login/")

def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'blog/Usuario_Detail.html', {'usuario': usuario})

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






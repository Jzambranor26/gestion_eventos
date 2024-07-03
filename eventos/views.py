from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm, EventoForm
from .models import Evento, Inscripcion
from django.contrib import messages


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al inicio de sesión después del registro exitoso
    else:
        form = RegistroForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('evento_list')  # Redirige a la lista de eventos después de iniciar sesión
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, inténtalo nuevamente.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al inicio de sesión después de cerrar sesión


@login_required
def evento_create_view(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.creador = request.user
            evento.save()
            return redirect('evento_list')
    else:
        form = EventoForm()
    return render(request, 'eventos/evento_create.html', {'form': form})


@login_required
def evento_list_view(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/evento_list.html', {'eventos': eventos})


@login_required
def evento_detail_view(request, pk):
    evento = Evento.objects.get(pk=pk)
    inscripciones = Inscripcion.objects.filter(evento=evento)
    inscripcion = Inscripcion.objects.filter(evento=evento, usuario=request.user).first()
    inscrito = True if inscripcion else False
    return render(request, 'eventos/evento_detail.html', {
        'evento': evento,
        'inscripciones': inscripciones,
        'inscripcion': inscripcion,
        'inscrito': inscrito,
    })


@login_required
def inscripcion_create_view(request, pk):
    evento = Evento.objects.get(pk=pk)
    Inscripcion.objects.get_or_create(evento=evento, usuario=request.user)
    return redirect('evento_detail', pk=pk)


@login_required
def inscripcion_delete_view(request, pk):
    inscripcion = Inscripcion.objects.get(pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('evento_detail', pk=inscripcion.evento.pk)
    return render(request, 'eventos/inscripcion_delete.html', {'inscripcion': inscripcion})


@login_required
def evento_delete_view(request, pk):
    evento = Evento.objects.get(pk=pk)
    if request.method == 'POST' and request.user == evento.creador:
        evento.delete()
        return redirect('evento_list')
    return render(request, 'eventos/evento_delete.html', {'evento': evento})


@login_required
def usuario_inscripciones_view(request):
    inscripciones = Inscripcion.objects.filter(usuario=request.user)
    return render(request, 'eventos/usuario_inscripciones.html', {'inscripciones': inscripciones})


@login_required
def index_view(request):
    if request.user.is_authenticated:
        return redirect('evento_list')


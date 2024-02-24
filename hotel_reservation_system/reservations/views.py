from django.shortcuts import render
from django.shortcuts import render, redirect
from hotel_reservation_system.reservations.models import Habitacion, Reserva

from django.shortcuts import render
from .models import Habitacion, Reserva
from django.http import HttpResponseRedirect

def buscar_habitaciones(request):
    if request.method == 'GET':
        return render(request, 'reservations/buscar_habitaciones.html')
    elif request.method == 'POST':
        fecha_entrada = request.POST.get('fecha_entrada')
        fecha_salida = request.POST.get('fecha_salida')
        habitaciones_disponibles = Habitacion.objects.filter(
            reserva__isnull=True
        ).exclude(
            reserva__fecha_entrada__lte=fecha_salida,
            reserva__fecha_salida__gte=fecha_entrada
        ).distinct()
        return render(request, 'reservations/buscar_habitaciones.html', {'habitaciones': habitaciones_disponibles, 'fecha_entrada': fecha_entrada, 'fecha_salida': fecha_salida})

def reservar_habitacion(request, habitacion_id):
    if request.method == 'POST':
        fecha_entrada = request.POST.get('fecha_entrada')
        fecha_salida = request.POST.get('fecha_salida')
        habitacion = Habitacion.objects.get(pk=habitacion_id)
        reserva = Reserva(habitacion=habitacion, fecha_entrada=fecha_entrada, fecha_salida=fecha_salida)
        reserva.save()
        return HttpResponseRedirect('/')  # Redirigir a la página principal o a donde desees después de la reserva

# views.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

# views.py
from django.db.models import Count

def estadisticas_ocupacion(request):
    habitaciones_reservadas = Reserva.objects.values('habitacion').annotate(total=Count('habitacion'))
    # Procesar los datos y pasarlos al template
    return render(request, 'estadisticas_ocupacion.html', {'habitaciones_reservadas': habitaciones_reservadas})


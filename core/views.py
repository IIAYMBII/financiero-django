from django.shortcuts import render, redirect
from .models import Ingreso, Gasto
from .forms import IngresoForm, GastoForm  
from django.db.models import Sum
from django.db.models.functions import TruncMonth
import json

from django.contrib.auth.models import User

def crear_admin():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='Axel',
            email='mendozabernalaxelyael551@gmail.com',
            password='F0RTANRTX9#'
        )
def dashboard(request):

    # Crear admin
    crear_admin()
    ingresos = Ingreso.objects.all()
    gastos = Gasto.objects.all()

    # Totales
    total_ingresos = sum(i.monto for i in ingresos)
    total_gastos = sum(g.monto for g in gastos)
    balance = total_ingresos - total_gastos

    # 📊 Gráfica simple
    fechas = [str(i.fecha) for i in ingresos]
    montos_ingresos = [float(i.monto) for i in ingresos]
    montos_gastos = [float(g.monto) for g in gastos]

    # 📅 Agrupación por mes
    ingresos_mes = (
        Ingreso.objects
        .annotate(mes=TruncMonth('fecha'))
        .values('mes')
        .annotate(total=Sum('monto'))
        .order_by('mes')
    )

    gastos_mes = (
        Gasto.objects
        .annotate(mes=TruncMonth('fecha'))
        .values('mes')
        .annotate(total=Sum('monto'))
        .order_by('mes')
    )

    labels_mes = [str(i['mes']) for i in ingresos_mes]
    datos_ingresos_mes = [float(i['total']) for i in ingresos_mes]
    datos_gastos_mes = [float(g['total']) for g in gastos_mes]

    # 🥧 Categorías
    gastos_categoria = (
        Gasto.objects
        .values('categoria__nombre')
        .annotate(total=Sum('monto'))
    )

    labels_cat = [g['categoria__nombre'] for g in gastos_categoria]
    datos_cat = [float(g['total']) for g in gastos_categoria]

    # 🐜 Gastos hormiga
    gastos_hormiga = Gasto.objects.filter(tipo='hormiga')
    total_hormiga = sum(g.monto for g in gastos_hormiga)
    cantidad_hormiga = gastos_hormiga.count()

    # 📊 Estadísticas
    promedio_gasto = total_gastos / gastos.count() if gastos.exists() else 0
    promedio_ingreso = total_ingresos / ingresos.count() if ingresos.exists() else 0

    return render(request, "dashboard.html", {
        "total_ingresos": total_ingresos,
        "total_gastos": total_gastos,
        "balance": balance,

        "fechas": json.dumps(fechas),
        "montos_ingresos": json.dumps(montos_ingresos),
        "montos_gastos": json.dumps(montos_gastos),

        "labels_mes": json.dumps(labels_mes),
        "datos_ingresos_mes": json.dumps(datos_ingresos_mes),
        "datos_gastos_mes": json.dumps(datos_gastos_mes),

        "labels_cat": json.dumps(labels_cat),
        "datos_cat": json.dumps(datos_cat),

        "total_hormiga": total_hormiga,
        "cantidad_hormiga": cantidad_hormiga,

        "promedio_gasto": promedio_gasto,
        "promedio_ingreso": promedio_ingreso,
    })


def ver_ingresos(request):
    ingresos = Ingreso.objects.all()
    return render(request, "ingresos.html", {"ingresos": ingresos})


def ver_gastos(request):
    gastos = Gasto.objects.all()
    return render(request, "gastos.html", {"gastos": gastos})


def crear_ingreso(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.usuario = request.user
            ingreso.save()
            return redirect('dashboard')
    else:
        form = IngresoForm()

    return render(request, 'crear_ingreso.html', {'form': form})


def crear_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.usuario = request.user
            gasto.save()
            return redirect('dashboard')
    else:
        form = GastoForm()

    return render(request, 'crear_gasto.html', {'form': form})
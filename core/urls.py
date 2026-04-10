from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard),
    path('ingresos/', views.ver_ingresos),
    path('gastos/', views.ver_gastos),
    path('nuevo-ingreso/', views.crear_ingreso, name='nuevo_ingreso'),
    path('nuevo-gasto/', views.crear_gasto, name='nuevo_gasto'),
]
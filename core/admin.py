from django.contrib import admin
from .models import Categoria, Ingreso, Gasto, Prestamo

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Ingreso)
admin.site.register(Gasto)
admin.site.register(Prestamo)



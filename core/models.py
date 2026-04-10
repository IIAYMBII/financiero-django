from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Ingreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    
    def __str__(self):
        return self.descripcion
    
class Gasto(models.Model):
    TIPOS = [
        ('Fijo', 'Fijo'),
        ('Variable','Variable'),
        ('Hormiga','Hormiga'),

    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    tipo = models.CharField(max_length=10,choices=TIPOS)
    fecha = models.DateField()
    

    def __str__(self):
        return self.descripcion
    
class Prestamo(models.Model):
    TIPOS = [
        ('deduda','deuda'),
        ('a favor', 'a favor')
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    persona = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField()

    def __str__(self):
        return self.persona
    


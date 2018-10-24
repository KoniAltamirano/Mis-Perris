from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class Usuario(models.Model):
    
    rut = models.CharField(max_length=12)
    nombre_completo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12,null=True)
    email = models.EmailField()
    region = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    tipo_vivienda = models.CharField(max_length=25)
    nombre_user = models.CharField(max_length=30)
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.rut

    class Meta:
        permissions = (
            ('usuario', _('Usuario')),
        )  


class Mascotas(models.Model):
    foto = models.ImageField(blank=True,null=True,upload_to="perro/%Y")
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    estado_choices = (
                     ('RESCATADO','Rescatado'),
                     ('DISPONIBLE','Disponible'),
                     ('ADOPTADO','Adoptado'),
    )
    estado = models.CharField(max_length=15,choices=estado_choices,default='RESCATADO')

    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


# Create your models here.

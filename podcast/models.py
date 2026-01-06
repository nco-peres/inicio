# Create your models here.

from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    lugar = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} ({self.fecha.year})"

class Podcast(models.Model):
    # Relación: Un evento puede tener varios podcasts
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='podcasts', null=True, blank=True)
    titulo = models.CharField(max_length=250)
    archivo_audio = models.FileField(upload_to='podcasts/')
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class Reel(models.Model):
    # Relación: Un evento puede tener varios reels
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='reels', null=True, blank=True)
    titulo = models.CharField(max_length=150)
    video = models.FileField(upload_to='reels/')
    miniatura = models.ImageField(upload_to='reels/thumbs/', blank=True)

    def __str__(self):
        return self.titulo
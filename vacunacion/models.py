from django.db import models


class provincias(models.Model):
    provincia = models.CharField(max_length=40)


class cantones(models.Model):
    canton = models.CharField(max_length=60)
    provincia = models.ForeignKey(provincias, on_delete=models.PROTECT, related_name="cantones")


class parroquias(models.Model):
    parroquia = models.CharField(max_length=85)
    canton = models.ForeignKey(cantones, on_delete=models.PROTECT, related_name="parroquias")


class centro_vacunacion(models.Model):
    canton = models.ForeignKey(cantones, on_delete=models.PROTECT, related_name="centro_vacunacion")
    centro_vacunacion = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)


class ciudadanos(models.Model):
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)
    cedula = models.CharField(max_length=10)
    provincia = models.ForeignKey(provincias, on_delete=models.PROTECT, related_name="ciudadanos")
    canton = models.ForeignKey(cantones, on_delete=models.PROTECT, related_name="ciudadanos")
    parroquia = models.ForeignKey(parroquias, on_delete=models.PROTECT, related_name="ciudadanos")
    centroVacunacion = models.ForeignKey(centro_vacunacion, on_delete=models.PROTECT, related_name="ciudadanos")
    primeraDosis = models.CharField(max_length=40)
    segundaDosis = models.CharField(max_length=40)

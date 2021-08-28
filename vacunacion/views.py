from rest_framework.views import APIView
from rest_framework.response import Response
from vacunacion.models import *


class Vacunacion(APIView):
    def post(self, request, format=None):
        if request.method == "POST":
            try:
                cedula = request.POST["cedula"]
                nombres = request.POST["nombres"].split()
                nombre1 = nombres[0]
                nombre2 = nombres[1]
                apellido1 = nombres[2]
                apellido2 = nombres[3]
                unCiudadano = ciudadanos.objects.get(cedula=cedula, nombre1=nombre1, nombre2=nombre2, apellido1=apellido1, apellido2=apellido2)
                json_consulta = {
                    "nombres": request.POST["nombres"],
                    "provincia": unCiudadano.provincia.provincia,
                    "canton": unCiudadano.canton.canton,
                    "centro_vacunacion": unCiudadano.centroVacunacion.centro_vacunacion,
                    "direccion": unCiudadano.centroVacunacion.direccion,
                    "primera_dosis": unCiudadano.primeraDosis,
                    "segunda_dosis": unCiudadano.segundaDosis,
                }
                return Response({"consulta": json_consulta})
            except ciudadanos.DoesNotExist:
                return Response({"mensaje": "Ups, no se encuentra registrado...."})

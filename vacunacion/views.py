from rest_framework.views import APIView
from rest_framework.response import Response
from vacunacion.models import *
from vacunacion.serializers import *
import json


class Vacunacion(APIView):
    def post(self, request, format=None):
        if request.method == "POST":
            try:
                json_data = json.loads(request.body.decode("utf-8"))
                cedula = json_data["cedula"]
                nombres = (json_data["nombres"]).split()
                nombre1 = nombres[0]
                nombre2 = nombres[1]
                apellido1 = nombres[2]
                apellido2 = nombres[3]
                unCiudadano = ciudadanos.objects.get(cedula=cedula, nombre1__icontains=nombre1, nombre2__icontains=nombre2, apellido1__icontains=apellido1, apellido2__icontains=apellido2)
                json_consulta = {
                    "nombres": json_data["nombres"].upper(),
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

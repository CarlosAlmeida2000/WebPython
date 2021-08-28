from django.urls import path
from vacunacion import views

urlpatterns = [
    path("consultar-lugar/", views.Vacunacion.as_view()),
]

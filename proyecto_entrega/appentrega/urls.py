from django.urls import path
from appentrega.views import *

urlpatterns = [
    path("", inicio,name="inicio"),
    path("requerimientos/",requerimientos, name='requerimientos'),
    path("crear_requerimiento/",crear_requerimiento, name='crear_requerimiento'),   
    path("crear_proyecto/",crear_proyecto, name='crear_proyecto'),
    path("crear_cliente/",crear_cliente, name='crear_cliente'),
    path("crear_colaborador/",crear_colaborador, name='crear_colaborador')
]
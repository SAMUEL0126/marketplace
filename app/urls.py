from django.urls import path , include
from .views import home , contacto , galeria ,\
     agregar_producto , listar_producto , modificar_producto ,\
         eliminar_producto , registro ,ProductoWiewset , MarcaViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto', ProductoWiewset)
router.register('marca', MarcaViewSet)



urlpatterns = [
    path('',home ,name="home"),
    path('contacto/',contacto ,name="contacto"),
    path('galeria/',galeria ,name="galeria"),
    path('agregar-producto/',agregar_producto ,name="agregar_producto"),
    path('listar-producto/',listar_producto ,name="listar_producto"),
    path('modificar-producto/<id>/',modificar_producto ,name="modificar_producto"),
    path('eliminar-producto/<id>/',eliminar_producto ,name="eliminar_producto"),
    path('registro/',registro ,name="registro"),
    path('api/',include(router.urls))
]
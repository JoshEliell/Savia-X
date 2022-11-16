from genericpath import exists
from itertools import count
from dashboard.models import ArticulosparaSurtir, Order
from requisiciones.models import Requis
from user.models import Profile
def contadores_processor(request):
    #Por si aun no se ingresa a un perfil para que no se trabe en el login
    usuario = Profile.objects.filter(staff__id=request.user.id).first()
    if not Profile.objects.filter(staff__id=request.user.id).first():
        productos= ArticulosparaSurtir.objects.filter(salida=False, articulos__orden__autorizar = True, articulos__producto__producto__servicio = False, articulos__orden__tipo__tipo="normal")
        ordenes_por_autorizar = Order.objects.filter(complete=True, autorizar=None)
    else:
        usuario = Profile.objects.filter(staff__id=request.user.id).first()
            #productos= ArticulosparaSurtir.objects.filter(salida=False, articulos__orden__autorizar = True, articulos__producto__producto__servicio = False, articulos__orden__tipo__tipo="normal")
            #productos= productos.filter(articulos__orden__superintendente=usuario)
        if usuario.tipo.superintendente == True:
            productos= Requis.objects.filter(complete=True, autorizar=None, orden__superintendente=usuario)
        elif usuario.tipo.almacenista == True:
            productos= Requis.objects.filter(complete=True, autorizar=None)
        else:
            productos = Requis.objects.filter(complete=None)           
        ordenes_por_autorizar = Order.objects.filter(complete=True, autorizar=None)
        ordenes_por_autorizar = ordenes_por_autorizar.filter(supervisor=usuario)
    #prod = []
    #for producto in productos:
        #if producto.articulos.orden not in prod:
        #    prod.append(producto.articulos.orden)
    conteo_pendientes = len(ordenes_por_autorizar)
    #conteo = len(prod)
    conteo = productos.count()

    return {
    'conteo_pendientes':conteo_pendientes,
    'conteodeordenes':conteo,
    'usuario':usuario,
    }
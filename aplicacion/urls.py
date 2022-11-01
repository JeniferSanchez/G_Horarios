from  django.urls import path
from .views import usuarioList

urlpatterns = [
    path('usuario/',usuarioList.as_view(), name ='usuario_list'),
]

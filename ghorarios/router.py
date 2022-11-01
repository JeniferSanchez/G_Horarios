from aplicacion.viewset import docenteViewset
from aplicacion.viewset import coordinadorViewset
from aplicacion.viewset import usuarioViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('docente',docenteViewset)
router.register('coordinador', coordinadorViewset)
router.register('usuario', usuarioViewset)

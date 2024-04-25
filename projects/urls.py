from rest_framework import routers
from .api import UsuarioViewSet, ProcesoViewSet, PlanMViewSet, ComiteViewSet, IniciarViewSet, GenerarViewSet, CitaViewSet 

router = routers.DefaultRouter()

router.register('api/usuario', UsuarioViewSet, 'usuario')

router.register('api/proceso', ProcesoViewSet, 'proceso')
router.register('api/planM', PlanMViewSet, 'planM')
router.register('api/comite', ComiteViewSet, 'comite')
router.register('api/iniciar', IniciarViewSet, 'iniciar')
router.register('api/generar', GenerarViewSet, 'generar')
router.register('api/cita', CitaViewSet, 'cita')

urlpatterns = router.urls
from rest_framework.routers import SimpleRouter
from .views import AlertViewSet, AlertResponseViewSet, AlertTypeViewSet

router = SimpleRouter()
router.register('alert-types', AlertTypeViewSet)
router.register('alerts', AlertViewSet)
router.register('responses', AlertResponseViewSet)

urlpatterns = router.urls

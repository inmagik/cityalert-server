from rest_framework.routers import SimpleRouter
from .views import AlertViewSet, AlertResponseViewSet

router = SimpleRouter()
router.register('alerts', AlertViewSet)
router.register('responses', AlertResponseViewSet)

urlpatterns = router.urls

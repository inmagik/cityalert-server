from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
    AlertViewSet, AlertResponseViewSet,
    AlertTypeViewSet, VoteAlertView, SimilarAlertsView
)

router = SimpleRouter()
router.register('alert-types', AlertTypeViewSet)
router.register('alerts', AlertViewSet)
router.register('responses', AlertResponseViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('vote-alert/<alert_id>/', VoteAlertView.as_view(), name="vote_alert"),
    path('similar-alerts/', SimilarAlertsView.as_view(), name="similar_alerts"),
]

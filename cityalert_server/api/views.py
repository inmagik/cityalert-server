from rest_framework.viewsets import ModelViewSet
from .serializers import AlertSerializer, AlertResponseSerializer
from alert.models import Alert, AlertResponse


class AlertViewSet(ModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()


class AlertResponseViewSet(ModelViewSet):
    serializer_class = AlertResponseSerializer
    queryset = AlertResponse.objects.all()

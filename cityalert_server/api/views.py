from rest_framework.viewsets import ModelViewSet
from .serializers import AlertSerializer, AlertResponseSerializer, AlertTypeSerializer, AlertType
from alert.models import Alert, AlertResponse


class AlertViewSet(ModelViewSet):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()


class AlertResponseViewSet(ModelViewSet):
    serializer_class = AlertResponseSerializer
    queryset = AlertResponse.objects.all()


class AlertTypeViewSet(ModelViewSet):
    serializer_class = AlertTypeSerializer
    queryset = AlertType.objects.all()

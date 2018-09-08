from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .serializers import AlertSerializer, AlertResponseSerializer, AlertTypeSerializer, AlertType
from alert.models import Alert, AlertResponse, AlertVote


class VoteAlertView(APIView):
    def post(self, request, alert_id):
        alert = Alert.objects.get(pk=alert_id)
        user = request.user
        alert_vote = AlertVote.objects.create(alert=alert, user=user)
        return Response(AlertSerializer(instance=alert, context={'request': request}).data)

class AlertViewSet(ModelViewSet):
    filter_fields = ('alert_type', )
    filter_backends = (SearchFilter,)
    search_fields = ('description', )
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()


class AlertResponseViewSet(ModelViewSet):
    serializer_class = AlertResponseSerializer
    queryset = AlertResponse.objects.all()


class AlertTypeViewSet(ModelViewSet):
    serializer_class = AlertTypeSerializer
    queryset = AlertType.objects.all()

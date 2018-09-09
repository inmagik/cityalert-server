from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AlertSerializer, AlertResponseSerializer, AlertTypeSerializer, AlertType
from alert.models import Alert, AlertResponse, AlertVote


class VoteAlertView(APIView):
    def post(self, request, alert_id):
        alert = Alert.objects.get(pk=alert_id)
        user = request.user
        alert_vote = AlertVote.objects.create(alert=alert, user=user)
        return Response(AlertSerializer(instance=alert, context={'request': request}).data)

class AlertViewSet(ModelViewSet):
    filter_fields = ('alert_type', 'response__status', )
    search_fields = ('description', )
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()

    def get_queryset(self):
        # if self.request.user.is_staff:
        #     return Alert.objects.exclude(response=None)
        return Alert.objects.all()


class AlertResponseViewSet(ModelViewSet):
    serializer_class = AlertResponseSerializer
    queryset = AlertResponse.objects.all()


class AlertTypeViewSet(ModelViewSet):
    serializer_class = AlertTypeSerializer
    queryset = AlertType.objects.all()


class SimilarAlertsView(APIView):
    def post(self, request):
        ser = AlertSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        similar_alerts = Alert.objects.filter(
            alert_type=ser.validated_data['alert_type']
        )
        out_ser = AlertSerializer(instance=similar_alerts, many=True, context={'request': request})
        return Response(out_ser.data)

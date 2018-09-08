from rest_framework import serializers
from alert.models import Alert, AlertResponse, AlertType


class AlertTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertType
        fields = "__all__"


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = "__all__"


class AlertResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertResponse
        fields = "__all__"

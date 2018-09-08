from rest_framework import serializers
from alert.models import Alert, AlertResponse, AlertType


class AlertTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertType
        fields = "__all__"


class AlertSerializer(serializers.ModelSerializer):

    alert_type_verbose = serializers.CharField(read_only=True, source='alert_type.name')

    class Meta:
        model = Alert
        fields = "__all__"
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        return Alert.objects.create(**validated_data, user=user)


class AlertResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertResponse
        fields = "__all__"

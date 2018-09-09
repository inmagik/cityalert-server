from rest_framework import serializers
from alert.models import Alert, AlertResponse, AlertType
from drf_extra_fields.fields import Base64ImageField

class AlertTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertType
        fields = "__all__"

class AlertSimilarSerializer(serializers.ModelSerializer):
    alert_type_verbose = serializers.CharField(read_only=True, source='alert_type.name')
    user_email = serializers.CharField(read_only=True, required=False, source='user.email')
    class Meta:
        model = Alert
        fields = "__all__"


class AlertResponseSerializer(serializers.ModelSerializer):
    related_alerts = serializers.PrimaryKeyRelatedField(queryset=Alert.objects.all(), many=True, required=False, write_only=True)

    class Meta:
        model = AlertResponse
        fields = "__all__"

    def create(self, validated_data):
        related_alerts = validated_data.pop('related_alerts')
        out = AlertResponse.objects.create(**validated_data)
        for alert in related_alerts:
            alert.response = out
            alert.save()
        return out


class AlertSerializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField()
    vote_by_me = serializers.SerializerMethodField()
    similar_alerts = serializers.SerializerMethodField()
    image = Base64ImageField(required=False)
    response = AlertResponseSerializer(read_only=True, required=False)
    user_email = serializers.CharField(read_only=True, required=False, source='user.email')
    assigned_office_verboser =  serializers.CharField(read_only=True, required=False, source='assigned_office.name')

    def get_similar_alerts(self, instance):
        return AlertSimilarSerializer(instance=instance.get_similar_alerts(), many=True).data

    def get_votes_count(self, instance):
        return instance.votes.count()

    def get_vote_by_me(self, instance):
        user = self.context['request'].user
        if not user.pk:
            return 0
        return instance.votes.filter(user=user).count() > 0

    alert_type_verbose = serializers.CharField(read_only=True, source='alert_type.name')

    class Meta:
        model = Alert
        fields = "__all__"
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        return Alert.objects.create(**validated_data, user=user)

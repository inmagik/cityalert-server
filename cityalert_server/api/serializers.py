from rest_framework import serializers
from alert.models import Alert, AlertResponse, AlertType


class AlertTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertType
        fields = "__all__"


class AlertSerializer(serializers.ModelSerializer):
    votes_count = serializers.SerializerMethodField()
    vote_by_me = serializers.SerializerMethodField()

    def get_votes_count(self, instance):
        return instance.votes.count()

    def get_vote_by_me(self, instance):
        user = self.context['request'].user
        return instance.votes.filter(user=user).count() > 0

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

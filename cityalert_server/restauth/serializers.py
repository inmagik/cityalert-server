from rest_framework.serializers import (
    ModelSerializer, Serializer, ValidationError, EmailField, CharField,
)
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'is_staff', )

class RecoverSerializer(Serializer):
    email = EmailField()

    def validate_email(self, email):
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("L'indirizzo email non è valido.")

        return email

class ResetSerializer(Serializer):
    password = CharField()

    def validate_password(self, password):
        validate_password(password)
        return password

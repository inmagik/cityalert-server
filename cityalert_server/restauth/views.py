from django.shortcuts import get_object_or_404
from django.core.signing import TimestampSigner, SignatureExpired, BadSignature
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template import loader
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from .serializers import (
    UserSerializer, RecoverSerializer, ResetSerializer,
)

User = get_user_model()


class MeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)


class RecoverView(APIView):
    def send_email(self, user, token):
        subject = 'Recupera Password'
        context = {
            'token': token,
            'base_url': settings.FRONTEND_URL,
        }
        from_email = settings.DEFAULT_FROM_EMAIL,
        body = loader.render_to_string('recover_email.txt', context).strip()
        send_mail(subject, body, from_email, [user.email])

    def post(self, request, *args, **kwargs):
        ser = RecoverSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        user = User.objects.get(email=ser.validated_data['email'])

        signer = TimestampSigner()
        token = signer.sign(user.pk)
        self.send_email(user, token)

        return Response(status=204)


class ParseTokenMixin(object):
    def parse_token(self, token):
        signer = TimestampSigner()
        try:
            return signer.unsign(token, max_age=259200)
        except BadSignature:
            raise ValidationError({ 'token': ['Link invalido'] })
        except SignatureExpired:
            raise ValidationError({ 'token': ['Link scaduto'] })


class CheckResetTokenView(APIView, ParseTokenMixin):
    def get(self, request, token, *args, **kwargs):
        self.parse_token(token)
        return Response(status=204)

class ResetView(APIView, ParseTokenMixin):
    def post(self, request, token, *args, **kwargs):
        user = get_object_or_404(User, pk=self.parse_token(token))

        ser = ResetSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        # activating user if it has no password (prevents activating real inactive users)
        if not user.password:
            user.is_active = True
        user.set_password(ser.validated_data['password'])
        user.save()

        return Response(status=204)

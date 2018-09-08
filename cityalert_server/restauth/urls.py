from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import (
    MeView, RecoverView, CheckResetTokenView, ResetView,
)

urlpatterns = [
    # auth
    path('me/', MeView.as_view(), name="me"),
    path('token-auth/', obtain_jwt_token, name="obtain_jwt_token"),
    path('token-refresh/', refresh_jwt_token, name="refresh_jwt_token"),
    # paswrd recover / reset
    path('recover-password/', RecoverView.as_view(), name="recover_password"),
    path('check-reset-token/<token>/', CheckResetTokenView.as_view(), name="check_reset_token"),
    path('reset-password/<token>/', ResetView.as_view(), name="reset_password"),
]

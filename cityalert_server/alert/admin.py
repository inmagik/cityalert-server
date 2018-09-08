from django.contrib import admin
from .models import AlertType, Alert, AlertResponse

admin.site.register(AlertResponse)
admin.site.register(AlertType)
admin.site.register(Alert)

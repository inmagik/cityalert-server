from django.contrib import admin
from .models import AlertType, Alert

admin.site.register(AlertType)
admin.site.register(Alert)

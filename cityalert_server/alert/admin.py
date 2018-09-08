from django.contrib import admin
from .models import AlertType, Alert, AlertResponse, AlertTypeRouting, Office

admin.site.register(Office)
admin.site.register(AlertTypeRouting)
admin.site.register(AlertResponse)
admin.site.register(AlertType)
admin.site.register(Alert)

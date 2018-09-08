from django.db import models


class AlertType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Alert(models.Model):
    alert_type = models.ForeignKey(AlertType, models.CASCADE, null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.id

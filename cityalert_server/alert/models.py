from django.contrib.gis.db import models
from django.conf import settings


class Office(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class AlertResponse(models.Model):
    """
    """
    STATUS_CHOICES = (
        ('accepted', 'Presa in carico'),
        ('resolved', 'Risolta'),
        ('invalid', 'Invalida'),
    )
    PRIORITY_CHOICES = (
        (1, 'Bassa'),
        (2, 'Media'),
        (3, 'Alta'),
    )

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='accepted')
    security_issue = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    message = models.TextField(blank=True, null=True)
    resolution_estimate_date = models.DateField(blank=True, null=True)


class AlertType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class AlertTypeRouting(models.Model):

    alert_type = models.OneToOneField(AlertType, models.CASCADE, null=True, blank=True)
    office = models.ForeignKey(Office, models.CASCADE, null=True, blank=True)


class Alert(models.Model):

    alert_type = models.ForeignKey(AlertType, models.CASCADE, null=True, blank=True)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)

    position = models.PointField(blank=True, null=True)
    location = models.CharField(blank=True, null=True, max_length=256)
    image = models.ImageField(blank=True, null=True)

    response = models.ForeignKey(AlertResponse, models.CASCADE, null=True, blank=True, related_name="alerts")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # will be set by server when saving the instance
    assigned_office = models.ForeignKey(Office, models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s" % self.id

    def save(self, *args, **kwargs):
        if not self.id:
            try:
                routing = AlertTypeRouting.objects.get(alert_type=self.alert_type)
                self.assigned_office = routing.office
            except AlertTypeRouting.DoesNotExist:
                pass
        return super(Alert, self).save(*args, **kwargs)


class AlertVote(models.Model):
    """
    Used to indicate that an user confirms an existing alert
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    alert = models.ForeignKey(Alert, models.CASCADE, related_name='votes')

    class Meta:
        unique_together = ('user', 'alert')

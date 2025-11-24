from django.db import models

class EstablishmentDetail(models.Model):
    tenant = models.OneToOneField("tenants.Establishment", on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tenant.name} Details"

from django.db import models

class Service(models.Model):
    tenant = models.ForeignKey("tenants.Establishment", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

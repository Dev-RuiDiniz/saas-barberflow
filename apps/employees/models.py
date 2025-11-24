from django.db import models

class Employee(models.Model):
    tenant = models.ForeignKey("tenants.Establishment", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)  # barbeiro, cabeleireiro etc.
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

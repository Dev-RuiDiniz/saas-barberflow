from django.db import models
from tenants.models import Establishment

class BaseTenantModel(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)

    class Meta:
        abstract = True

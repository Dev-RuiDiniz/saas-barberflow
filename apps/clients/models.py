from django.db import models

class Client(models.Model):
    tenant = models.ForeignKey("tenants.Establishment", on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

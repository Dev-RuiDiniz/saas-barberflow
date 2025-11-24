from django.db import models

class Scheduling(models.Model):
    tenant = models.ForeignKey("tenants.Establishment", on_delete=models.CASCADE)
    client = models.ForeignKey("apps.clients.Client", on_delete=models.CASCADE)
    employee = models.ForeignKey("apps.employees.Employee", on_delete=models.CASCADE)
    service = models.ForeignKey("apps.services.Service", on_delete=models.CASCADE)

    datetime = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pendente"),
            ("confirmed", "Confirmado"),
            ("canceled", "Cancelado"),
        ],
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Agendamento {self.client.name} - {self.datetime}"

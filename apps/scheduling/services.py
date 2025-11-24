from .models import Scheduling   # <-- IMPORT NECESSÁRIO!


def create_scheduling(tenant, validated_data):
    return Scheduling.objects.create(tenant=tenant, **validated_data)

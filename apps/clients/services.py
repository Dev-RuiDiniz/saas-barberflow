from .models import Client

def create_client(tenant, validated_data):
    return Client.objects.create(tenant=tenant, **validated_data)

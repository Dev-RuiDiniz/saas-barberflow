from rest_framework import generics
from core.permissions import IsTenantUser
from core.utils import tenant_filter
from .models import Client
from .serializers import ClientSerializer
from .services import create_client


class ClientListCreateView(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return tenant_filter(Client.objects.all(), self.request.tenant)

    def perform_create(self, serializer):
        create_client(self.request.tenant, serializer.validated_data)


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return tenant_filter(Client.objects.all(), self.request.tenant)

from rest_framework import generics
from core.permissions import IsTenantUser
from core.utils import tenant_filter
from .models import Service
from .serializers import ServiceSerializer
from .services import create_service


class ServiceListCreateView(generics.ListCreateAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return tenant_filter(Service.objects.all(), self.request.tenant)

    def perform_create(self, serializer):
        create_service(self.request.tenant, serializer.validated_data)


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return tenant_filter(Service.objects.all(), self.request.tenant)

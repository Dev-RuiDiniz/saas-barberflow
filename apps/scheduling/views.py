from rest_framework import generics
from core.permissions import IsTenantUser
from core.utils import tenant_filter
from .models import Scheduling
from .serializers import SchedulingSerializer
from .services import create_scheduling


class SchedulingListCreateView(generics.ListCreateAPIView):
    serializer_class = SchedulingSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return tenant_filter(Scheduling.objects.all(), self.request.tenant)

    def perform_create(self, serializer):
        create_scheduling(self.request.tenant, serializer.validated_data)


class SchedulingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SchedulingSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return tenant_filter(Scheduling.objects.all(), self.request.tenant)

from rest_framework import generics
from core.permissions import IsTenantUser
from core.utils import tenant_filter
from .models import Employee
from .serializers import EmployeeSerializer
from .services import create_employee


class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return tenant_filter(Employee.objects.all(), self.request.tenant)

    def perform_create(self, serializer):
        create_employee(self.request.tenant, serializer.validated_data)


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return tenant_filter(Employee.objects.all(), self.request.tenant)

import pytest
from django.contrib.auth import get_user_model
from tenants.models import Establishment
from apps.clients.models import Client
from apps.employees.models import Employee
from apps.services.models import Service
from apps.scheduling.models import Scheduling

User = get_user_model()


@pytest.fixture
def tenant(db):
    return Establishment.objects.create(
        name="Barbearia Teste",
        subdomain="test",
        cnpj="11122233344",
    )


@pytest.fixture
def user(db):
    return User.objects.create_user(
        email="user@test.com",
        password="123456"
    )


@pytest.fixture
def client(tenant):
    return Client.objects.create(
        tenant=tenant,
        name="Cliente Teste",
        email="cliente@test.com"
    )


@pytest.fixture
def employee(tenant):
    return Employee.objects.create(
        tenant=tenant,
        name="Funcionario Test",
        role="Barbeiro"
    )


@pytest.fixture
def service(tenant):
    return Service.objects.create(
        tenant=tenant,
        name="Corte Masculino",
        duration=30,
        price=50
    )


@pytest.fixture
def scheduling(tenant, client, employee, service):
    return Scheduling.objects.create(
        tenant=tenant,
        client=client,
        employee=employee,
        service=service,
        datetime="2025-01-01T10:00:00Z"
    )

from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    return APIClient()

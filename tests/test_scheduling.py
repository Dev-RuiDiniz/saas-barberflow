from django.urls import reverse

def test_create_scheduling(api_client, tenant, client, employee, service):
    url = reverse("scheduling:list")

    data = {
        "client": client.id,
        "employee": employee.id,
        "service": service.id,
        "datetime": "2025-01-01T10:00:00Z"
    }

    api_client.credentials(HTTP_X_TENANT=tenant.id)

    resp = api_client.post(url, data)

    assert resp.status_code == 201
    assert resp.data["status"] == "pending"


def test_prevent_overlapping_scheduling(api_client, tenant, scheduling):
    url = reverse("scheduling:list")

    api_client.credentials(HTTP_X_TENANT=tenant.id)

    data = {
        "client": scheduling.client.id,
        "employee": scheduling.employee.id,
        "service": scheduling.service.id,
        "datetime": scheduling.datetime
    }

    resp = api_client.post(url, data)

    # se sua regra bloquear, deve ser 400
    assert resp.status_code == 400

from django.urls import reverse

def test_public_fetch_services(api_client, tenant):
    url = reverse("public_api:services", kwargs={"subdomain": tenant.subdomain})
    resp = api_client.get(url)

    assert resp.status_code == 200
    assert isinstance(resp.data, list)

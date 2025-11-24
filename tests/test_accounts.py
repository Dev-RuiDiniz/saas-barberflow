from django.urls import reverse

def test_user_login(api_client, user):
    resp = api_client.post(reverse("accounts:login"), {
        "email": "user@test.com",
        "password": "123456"
    })
    assert resp.status_code == 200
    assert "access" in resp.data

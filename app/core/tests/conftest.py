import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def user():
    return get_user_model().objects.create_user(
        username="TestUser",
        password="testpass",
    )


@pytest.fixture
def admin():
    return get_user_model().objects.create_user(
        is_staff=True,
        username="TestAdminUser",
        password="testadmin",
    )


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_client(user, client):
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def admin_client(admin, client):
    client.force_authenticate(user=admin)
    return client
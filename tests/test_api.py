import pytest
from api.endpoints import Endpoints

@pytest.mark.api
@pytest.mark.smoke
def test_get_users_list_status_and_schema(api_client):
    """
    API Smoke Test: Verify GET /users returns HTTP 200 with pagination data.
    """
    response = api_client.get(Endpoints.USERS, params={"page": 2})

    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    
    data = response.json()
    assert "page" in data and data["page"] == 2
    assert "data" in data and isinstance(data["data"], list)
    assert len(data["data"]) > 0, "Users list should not be empty"

    # Validate schema fields of the first user record
    first_user = data["data"][0]
    for key in ["id", "email", "first_name", "last_name", "avatar"]:
        assert key in first_user, f"Missing expected field '{key}' in user object"

@pytest.mark.api
@pytest.mark.regression
def test_create_user_post_request(api_client):
    """
    API Regression Test: Verify POST /users creates new resource and returns 201 Created.
    """
    payload = {
        "name": "Alex QA Lead",
        "job": "Automation Architect"
    }

    response = api_client.post(Endpoints.USERS, json=payload)

    assert response.status_code == 201, f"Expected 201 but got {response.status_code}"
    
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["job"] == payload["job"]
    assert "id" in data, "Created record must return an ID"
    assert "createdAt" in data, "Created record must have a timestamp"

@pytest.mark.api
@pytest.mark.regression
def test_user_not_found_negative_scenario(api_client):
    """
    API Negative Test: Verify GET on non-existent user returns HTTP 404.
    """
    endpoint = Endpoints.SINGLE_USER.format(user_id=99999)
    response = api_client.get(endpoint)

    assert response.status_code == 404, f"Expected 404 for invalid user ID but got {response.status_code}"

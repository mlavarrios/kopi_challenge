def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == "The health check is OK."
import uuid

from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_github_skills_activity_is_available():
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert "GitHub Skills" in activities


def test_can_sign_up_for_github_skills_activity():
    email = f"student-{uuid.uuid4().hex}@mergington.edu"
    response = client.post(
        f"/activities/GitHub Skills/signup?email={email}"
    )

    assert response.status_code == 200
    assert response.json()["message"].startswith(f"Signed up {email} for GitHub Skills")

from app import app

def test_pass():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Flask CI/CD" in response.data  # ✅ Test đúng

#def test_fail():
#  client = app.test_client()
#  response = client.get('/')
#  assert b"Sai noi dung" in response.data  # ❌ Test sai cố ý
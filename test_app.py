from app import add, app

def test_add():
    assert add(2, 3) == 5

def test_home():
    client = app.test_client()
    assert client.get("/").status_code == 200

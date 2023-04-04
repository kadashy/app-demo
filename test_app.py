import json
from app import app

def test_probe_healthy():
    client = app.test_client()

    response = client.get('/probe/healthy')

    data = json.loads(response.data)

    assert data['status'] == 'up'

    assert data['Env 1'] == 'value_1'

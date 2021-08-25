from datetime import datetime, timezone, timedelta

import pytest
from sanic.websocket import WebSocketProtocol

from main import app

moscow_tz = timezone(timedelta(hours=3))


@pytest.fixture
def test_app(loop, sanic_client):
    return loop.run_until_complete(sanic_client(app, protocol=WebSocketProtocol))


async def test_time_correctness(test_app):
    current_time = datetime.now(tz=moscow_tz)
    response = await test_app.get('/')
    assert response.status_code == 200
    assert current_time.strftime('%H:%M:%S') == response.text

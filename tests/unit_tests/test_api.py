import pytest
from server import create_app


# Фикстура для aiohttp
@pytest.fixture
async def client(aiohttp_client):
    app = create_app()
    return await aiohttp_client(app)


async def test_healthcheck(client):
    resp = await client.get("/healthcheck")
    assert resp.status == 200
    text = await resp.text()
    assert text == "{}"


async def test_hash_string_success(client):
    payload = {"string": "test"}
    resp = await client.post("/hash", json=payload)
    assert resp.status == 200
    text = await resp.json()
    assert "hash_string" in text


async def test_hash_string_missing_field(client):
    resp = await client.post("/hash", json={})
    assert resp.status == 400
    text = await resp.json()
    assert "validation_errors" in text


async def test_hash_string_invalid_json(client):
    resp = await client.post("/hash", data="not a json")
    assert resp.status == 500
    text = await resp.json()
    assert "Ошибка" in text

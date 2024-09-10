import pytest
from httpx import AsyncClient
from app.main import app  # Adjust the import according to your file structure

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}

@pytest.mark.asyncio
async def test_read_page1():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/page1")
        assert response.status_code == 200
        assert response.json() == {"message": "Page 1"}

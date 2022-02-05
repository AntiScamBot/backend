import pytest
from ..api import app

# Dummy datas
DUMMY_DOMAIN = "example.com"

class TestEverything:
    async def check_client(self):
        pass

    @pytest.fixture
    def client():
        with app.test_client() as client:
            yield client
        
    def test_statuscode(client):
        """
        Tests /api/check API: Correct credentials
        """
        response = client.post(f'/api/check/{DUMMY_DOMAIN}')
        return response.text()

    @pytest.mark.asyncio
    async def pytest_sessionfinish(self):
        """Closes the session at the end of the tests"""
        await pytest.exit("succesfull exited")

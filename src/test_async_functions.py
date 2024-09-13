import pytest
from async_functions import fetch_data

@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result == {"data": "sample data"}
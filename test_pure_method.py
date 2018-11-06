# content of test_caching.py
import pytest
import time


@pytest.fixture
def fixture_data00(request):
    val = request.config.cache.get("example/value", None)
    if val is None:
        time.sleep(9*0.6) # expensive computation :)
        val = 42
        request.config.cache.set("example/value", val)
    return val


def test_function(fixture_data00):
    assert fixture_data00 == 23

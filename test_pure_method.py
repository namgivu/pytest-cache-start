import pytest


def setUpModule():
    """create cache via @pytest.fixture methods"""
    pass

def tearDownModule():
    pass #TODO clear cache here


@pytest.fixture
def fixture_data00(request):
    v = request.config.cache.get('example/value', None)
    if v is None:
        import time; time.sleep(9*0.6); v = 122 # mock it as if it is an expensive computation :)
        request.config.cache.set('example/value', v)
    return v


def test_that_fail(fixture_data00):
    assert fixture_data00 == 333


def test_that_pass(fixture_data00):
    assert fixture_data00 == 122

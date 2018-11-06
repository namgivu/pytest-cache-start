import pytest
import unittest


def setUpModule(): pass # nothing here - cache(s) are created with @pytest.fixture method(s)

def tearDownModule(): pass # nothing here - cache(s) are cleared
                           # either by 1) manually by `pytest --cache-view`
                           # or by 2) automatically @pytest.fixture(scope='module')

v = None

@pytest.fixture(scope='module') # ref. https://docs.pytest.org/en/latest/fixture.html#scope-sharing-a-fixture-instance-across-tests-in-a-class-module-or-session
def fixture_data00(request):
    global v
    v = request.config.cache.get('example/value', None)
    if v is None:
        print('\nCache for :v not found - creating value for it...')
        import time; time.sleep(9*0.6); v = 122 # mock it as if it is an expensive computation :)
        request.config.cache.set('example/value', v)
        print('Cache for :v not found - creating value for it... Done')


@pytest.mark.usefixtures('fixture_data00') # ref. https://docs.pytest.org/en/latest/fixture.html#using-fixtures-from-classes-modules-or-projects
class TestPytestCache(unittest.TestCase):

    def setUp(self): pass # currently nothing here

    def tearDown(self): pass # currently nothing here


    def test_that_fail(self):
        global v
        assert v == 333


    def test_that_pass(self):
        global v
        assert v == 122


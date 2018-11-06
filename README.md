#ref.
[guide 0th](https://docs.pytest.org/en/latest/cache.html)
[use with test class](https://docs.pytest.org/en/latest/fixture.html#using-fixtures-from-classes-modules-or-projects)

#noticeable points

##01
> This plugin is enabled by default

##02 fixture cache 
ref. https://docs.pytest.org/en/latest/cache.html#the-new-config-cache-object
when running a test method, we often *clear tables and re-fill it* against test database
those works can be cached to speed up time

this feature means running a single test at the 2nd time, the cached values are kept remained
> If you run it a second time the value will be retrieved from the cache and this will be quick:
so very likely we can reduce fixture creation as our current need

sample code
```python
# content of test_caching.py
import pytest
import time

@pytest.fixture
def mydata(request):
    val = request.config.cache.get("example/value", None)
    if val is None:
        time.sleep(9*0.6) # expensive computation :)
        val = 42
        request.config.cache.set("example/value", val)
    return val

def test_function(mydata):
    assert mydata == 23
```

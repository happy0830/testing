import pytest
import yaml

@pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
class TestCal():
    # @pytest.fixture("add")
    def test_add(self,a,b):
        return a + b
        print(a+b)

    # @pytest.fixture("div")
    def test_div(self,a,b):
        if b == 0:
            raise ZeroDivisionError
        else:
            return a/b
            print(a/b)

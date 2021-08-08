

import pytest
import yaml
import decimal


class Cal():
    def __int__(self,a,b):
        self.a=a
        self.b=b

    def add(self,a,b):
        return a+b
    def div(self,a,b):
        if b == 0:
            raise ZeroDivisionError
        else:
            return a/b


@pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data.yaml")))
class TestCal():
    # def setup(self):
    #     self.cal=Cal()
    # @pytest.mark.ADD
    @pytest.mark.run(order=2)
    def test_add(self,a,b):
        result=Cal().add(a,b)
        return result
        print("result")

    # @pytest.mark.DIV
    @pytest.mark.run(order=1)
    def test_div(self,a,b):
        result= Cal().div(a,b)
        return result
        print(result)


import math_1
import pytest

@pytest.mark.parametrize("test_input,ex_result",[(1,1),(2,4),(3,9),(4,16)])
def test_func(test_input,ex_result):
    Result=math_1.sqr(test_input)
    assert Result==ex_result

@pytest.mark.parametrize("test_input0,test_input1,ex_result",[(1,1,2),(2,4,6)])
def test_add(test_input0,test_input1,ex_result):
    Result=math_1.add(test_input0,test_input1)
    assert Result==ex_result

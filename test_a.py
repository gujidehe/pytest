import pytest


def func(x):
    x+=1
    return x
    print(x)
def test_answer():
    assert func(3) == 4

if __name__ == '__main__':
    pytest.main(['-vs','test_a.py'])
from mathp import add ,sub

def test_positive():
    assert add(2, 3) == 5

def test_negative():
    assert add(-2, -3) == -5

def test_sub():
    assert sub(3,4)==-2

from hello import hello

def test_defualt():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Ana") == "hello, Ana"


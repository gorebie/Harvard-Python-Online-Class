from hello import hello

def test_hello():
    hello("Ana") == "hello, Ana"

def test_argument():
    assert hello("Ana") == "hello, Ana"
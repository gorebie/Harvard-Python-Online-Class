from hello import hello

def test_hello():
    hello("Ana") == "hello, Ana"

def test_argument():
    for name in ["Lucky", "Enzo"]:
        assert hello("Ana") == f"hello, {name}"
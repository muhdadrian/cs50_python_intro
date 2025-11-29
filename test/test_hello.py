from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"

#pytest test -- 'test' is the test folder -- testing the folder
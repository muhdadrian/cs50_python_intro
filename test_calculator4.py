from calculator4 import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0




# pytest -- 3rd party library for unit test automatically.
# unit test is typically test for function.
# pytest is not user-friendly, as it only gives you clue of the bug.
# pip install pytest.
# Type: pytest test_calculator4.py in terminal not python at the beginning.

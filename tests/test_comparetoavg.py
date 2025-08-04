# tests/test_comparetoavg.py
from src.comparetoavg import compareToAvg

def test_compare_mixed(capsys):
	"""
	Verifies output for numbers less than, equal to, and greater than average.
	"""
	compareToAvg(4, 5, 6, 5)
	captured = capsys.readouterr()
	assert "4 is less than the average 5" in captured.out
	assert "5 is equal to the average 5" in captured.out
	assert "6 is greater than the average 5" in captured.out

# 2 data sets of all three values are equal to the average
def test_compare_all_equal(capsys):
    """
    Tests inputs: (7, 7, 7) with avg
    """
    compareToAvg(7, 7, 7, 7)
    captured = capsys.readouterr()
    assert "7 is equal to the average" in captured.out
    assert "7 is equal to the average" in captured.out
    assert "7 is equal to the average" in captured.out
    

def test_compare_all_equal_1(capsys):
    """
    Tests inputs: (10, 10, 10) with avg
    """
    compareToAvg(10, 10, 10, 10)
    captured = capsys.readouterr()
    assert "10 is equal to the average" in captured.out
    assert "10 is equal to the average" in captured.out
    assert "10 is equal to the average" in captured.out
   

# 3 sets where no values is equal to the average
def test_compare_none_equal(capsys):
    """
    Tests input: (2, 4, 8) with avg = 4.667
    No values are equal to the average.
    """
    compareToAvg(1, 2, 7, 3.333)
    captured = capsys.readouterr()
    assert "1 is less than the average 3.333" in captured.out
    assert "2 is less than the average 3.333" in captured.out
    assert "7 is greater than the average 3.333" in captured.out


def test_compare_none_equal_1(capsys):
    """
    Tests input: (-5, 6, -8) with avg = -2.333
    None of the values are equal to the average.
    """
    compareToAvg(-5, 6, -8, -2.333)
    captured = capsys.readouterr()
    assert "-5 is less than the average -2.333" in captured.out
    assert "6 is greater than the average -2.333" in captured.out
    assert "-8 is less than the average -2.333" in captured.out

def test_compare_none_equal_2(capsys):
    """
    Tests input: (1, 3, 8) with avg = 4
    No values are equal to the average.
    """
    compareToAvg(1, 3, 8, 4)
    captured = capsys.readouterr()
    assert "1 is less than the average 4" in captured.out
    assert "3 is less than the average 4" in captured.out
    assert "8 is greater than the average 4" in captured.out

#  5 sets where one item is equal to the average
def test_compare_one_equal_1(capsys):
    """
    One value equals avg: middle value equals.
    Inputs: (4, 5, 6), avg = 5
    """
    compareToAvg(4, 5, 6, 5)
    captured = capsys.readouterr()
    assert "4 is less than the average 5" in captured.out
    assert "5 is equal to the average 5" in captured.out
    assert "6 is greater than the average 5" in captured.out

def test_compare_one_equal_2(capsys):
    """
    One value equals avg: middle value equals.
    Inputs: (9, 10, 11), avg = 10
    """
    compareToAvg(9, 10, 11, 10)
    captured = capsys.readouterr()
    assert "9 is less than the average 10" in captured.out
    assert "10 is equal to the average 10" in captured.out
    assert "11 is greater than the average 10" in captured.out

def test_compare_one_equal_3(capsys):
    """
    One value equals avg: middle value equals.
    Inputs: (1, 2, 3), avg = 2
    """
    compareToAvg(1, 2, 3, 2)
    captured = capsys.readouterr()
    assert "1 is less than the average 2" in captured.out
    assert "2 is equal to the average 2" in captured.out
    assert "3 is greater than the average 2" in captured.out

def test_compare_one_equal_4(capsys):
    """
    One value equals avg: middle value equals (with float).
    Inputs: (4.5, 5.5, 6.5), avg = 5.5
    """
    compareToAvg(4.5, 5.5, 6.5, 5.5)
    captured = capsys.readouterr()
    assert "4.5 is less than the average 5.5" in captured.out
    assert "5.5 is equal to the average 5.5" in captured.out
    assert "6.5 is greater than the average 5.5" in captured.out

def test_compare_one_equal_case_5(capsys):
    """
    One value equals avg: middle value equals (larger numbers).
    Inputs: (100, 200, 300), avg = 200
    """
    compareToAvg(100, 200, 300, 200)
    captured = capsys.readouterr()
    assert "100 is less than the average 200" in captured.out
    assert "200 is equal to the average 200" in captured.out
    assert "300 is greater than the average 200" in captured.out


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

    

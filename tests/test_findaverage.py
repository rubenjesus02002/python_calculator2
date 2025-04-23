# tests/test_findaverage.py
from src.findaverage import findaverage

def test_findaverage():
    """
    Tests correct calculation of averages.
    """
    assert findaverage(3, 3, 3) == 3.0
    assert findaverage(1, 2, 3) == 2.0
    assert findaverage(1, 2, 2) == 1.667

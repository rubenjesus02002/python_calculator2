# tests/test_introduction.py
from src.introduction import introduction

def test_introduction_output(capsys):
    """
    Tests the printed output of introduction().
    """
    introduction()
    captured = capsys.readouterr()
    expected = (
        "This program prompts the user to enter 3 integers values.\n"
        "The program then finds the average of these 3 values.\n"
        "It then compares them to the average and prints an appropriate message.\n"
    )
    assert captured.out == expected
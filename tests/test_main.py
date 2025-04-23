# tests/test_main.py
from src.main import main

def test_main_flow(monkeypatch, capsys):
    """
    Simulates full program run with input. Checks output.
    """
    simulated_input = iter([
        "1", "2", "3",
        "3", "3", "3",
        "4", "5", "6",
        "2", "2", "2",
        "10", "20", "30",
        "7", "7", "7",
        "9", "8", "7",
        "5", "5", "5",
        "1", "1", "1",
        "0", "0", "0"
    ])
    monkeypatch.setattr("builtins.input", lambda _: next(simulated_input))
    main()
    captured = capsys.readouterr()
    assert "The average is" in captured.out

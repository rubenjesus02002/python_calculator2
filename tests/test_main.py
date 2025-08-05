from types import SimpleNamespace
def test_main(monkeypatch, capsys):
    """
    Simulates full program run with input. Checks output.
    """

    simulated_input = iter({
        "4", "4", "4",
        "5", "5", "5",
        "5", "8", "11",
        "9", "3", "15",
        "4", "1",  "7",
        "10", "20", "30",
        "12", "2", "7",
        "4", "5",  "7",
        "6", "8", "9",
        "2", "6", "7"
    })

    monkeypatch.setattr("builtins.input", lambda _: next(simulated_input))

    main()
    captured = capsys.readouterr()
    assert "The average is" in captured.out

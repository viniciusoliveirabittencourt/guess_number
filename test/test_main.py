from unittest.mock import patch
from main import menu


def test_analyzer_menu_basic(capsys):
    def fake_input(prompt=""):
        print(prompt, end=" ")
        return ""

    with patch("builtins.input", fake_input):
        menu()
    out, _ = capsys.readouterr()
    assert (
        "Please, select one of the options below:\n"
        "1 - AI guess the number\n"
        "2 - Player guess the number\n"
        "3 - Player X AI\n"
        "4 - Player X Player\n"
        "0 - Leave\n"
        "Input value: "
        in out
    )

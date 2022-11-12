from main import main


def test_menu_print_options(capsys):
    main()
    captured = capsys.readouterr()
    expected = (
        "Please, select one of the options below:"
        "1 - AI guess the number"
        "2 - Player guess the number"
        "3 - Player X AI"
        "4 - Player X Player"
        "0 - Leave"
    )

    assert captured.out == expected

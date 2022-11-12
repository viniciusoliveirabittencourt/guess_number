from main import main


def test_menu(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "working!\nGoodbye :)\n"

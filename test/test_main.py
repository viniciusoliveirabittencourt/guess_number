from main import main


def test_menu_print_options(capsys):

    main()

    caps = capsys.readouterr()

    assert (
        "Please, select one of the options below:\n"
        "1 - AI guess the number\n"
        "2 - Player guess the number\n"
        "3 - Player X AI\n"
        "4 - Player X Player\n"
        "0 - Leave\n"
        "Input value: \n"
    ) == caps.out

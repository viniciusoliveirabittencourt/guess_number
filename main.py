def menu():
    menu_user_input = input(
        "Please, select one of the options below:\n"
        "1 - AI guess the number\n"
        "2 - Player guess the number\n"
        "3 - Player X AI\n"
        "4 - Player X Player\n"
        "0 - Leave\n"
        "Input value: "
    )

    return menu_user_input


if __name__ == "__main__":
    menu()

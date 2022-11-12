def main():
    user_option = None

    while user_option != 0:
        try:
            input(
                "Please, select one of the options below:\n"
                "1 - AI guess the number\n"
                "2 - Player guess the number\n"
                "3 - Player X AI\n"
                "4 - Player X Player\n"
                "0 - Leave\n"
            )
            break
        except ValueError:
            raise ValueError

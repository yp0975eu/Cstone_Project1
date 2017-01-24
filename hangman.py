import display


class Main:

    word = None
    file_name = 'words.txt'

    def __init__(self):

        self.word = self.select_word()

    def start_game(self):

        # dictionary from: https://www.flocabulary.com/5th-grade-vocabulary-word-list/
        word = self.select_word()

        display.Display.show_game_board(word)

        self.game_loop()

    def game_loop(self):
        import string

        game_status = True

        # https://docs.python.org/3/library/string.html#string-constants

        available_letters = list(string.ascii_lowercase)

        guessed_letters = []

        display.Display.show_available_letters(available_letters, guessed_letters)

        while game_status:

            display.Display.guess_letter_message()

            guess = input('\n')

            while guess not in available_letters:

                guess = input('\nThat\'s not a valid guess.')

            if guess in self.word:

                print(guess)

                print(self.word)

            else:

                print('bad guess')

    # get menu option
    def select_menu_option(self):

        selection = input("\n")

        while selection not in ['1', '2']:

            selection = input("\n")

        if selection == '1':

            self.start_game()

        elif selection == '2':

            exit()

    # selects random word from words.txt
    def select_word(self):
        import random
        i = 0

        # get line count
        # http://stackoverflow.com/q/845058
        with open(self.file_name) as f:
            for i, l in enumerate(f):
                pass

        file = open(self.file_name, "r")

        lines = file.readlines()

        return lines[random.randint(0, i)]

    # main function
    def run(self):

        display.Display.welcome_menu()

        self.select_menu_option()


if __name__ == "__main__":
    m = Main()
    m.run()

import display


class Main:

    file_name = 'words.txt'

    def __init__(self):
        self.letter_counter = None
        self.bad_guesses = None
        self.word = None

    def start_game(self):

        self.letter_counter = self.word = self.select_word()

        self.bad_guesses = 7

        # create a set for tracking valid guess, remove a valid guess and check for winning status by checking len
        self.letter_counter = set(self.letter_counter)

        # print(self.word)

        # print(self.letter_counter)

        # dictionary from: https://www.flocabulary.com/5th-grade-vocabulary-word-list/
        display.Display.show_game_board(self.word)

        self.game_loop()

    def game_loop(self):
        import string

        game_status = True

        # https://docs.python.org/3/library/string.html#string-constants

        available_letters = list(string.ascii_lowercase)

        guessed_letters = []

        # TODO: add winning logic

        while game_status:

            display.Display.guess_letter_message()

            display.Display.show_available_letters(available_letters)

            guess = input('\n')

            while guess not in available_letters:

                guess = input('\nThat\'s not a valid guess.\n')

            if guess in self.word:

                available_letters.remove(guess)

                guessed_letters.append(guess)

                self.letter_counter.remove(guess)

                display.Display.show_correct_guessed_letters(self.word, guessed_letters)

            else:

                self.bad_guesses -= 1

                if self.bad_guesses <= 0:

                    game_status = False

                    print('game over')

                else:

                    available_letters.remove(guess)

                    print('bad guess')

                    display.Display.show_correct_guessed_letters(self.word, guessed_letters)

            if len(self.letter_counter) == 0:

                print("You win")

                game_status = False

        # restart game

        self.run()

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

        return lines[random.randint(0, i)].strip()

    # main function
    def run(self):

        display.Display.welcome_menu()

        self.select_menu_option()


if __name__ == "__main__":
    m = Main()
    m.run()

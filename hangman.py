import display


class Main:

    file_name = 'words.txt'

    def __init__(self):
        self.target_letters = None
        self.words = []
        self.bad_guesses = 7
        self.target_word = None
        self.available_letters = None
        self.guessed_letters = None

        # get line count
        # load line into class words attribute
        with open(self.file_name, "r") as file:
            self.words = file.readlines()

    def start_game(self):

        self.game_loop()

    def game_loop(self):

        game_status = True

        self.reset_game()

        print(self.target_word)

        display.game_board(self.target_word)

        while game_status:

            # dictionary from: https://www.flocabulary.com/5th-grade-vocabulary-word-list/

            display.guess_letter_message()

            display.available_letters(self.available_letters)

            guess = input('\n')

            while guess not in self.available_letters:

                guess = input('\nThat\'s not a valid guess.\n')

            if guess in self.target_letters:

                self.available_letters.remove(guess)

                self.guessed_letters.append(guess)

                self.target_letters.remove(guess)

                display.correct_guessed_letters(self.target_word, self.guessed_letters)

            else:

                self.bad_guesses -= 1

                if self.bad_guesses <= 0:

                    game_status = False

                    print('game over')

                else:

                    self.available_letters.remove(guess)

                    print('bad guess. {} guesses remaining'.format(self.bad_guesses))

                    display.correct_guessed_letters(self.target_word, self.guessed_letters)

            if len(self.target_letters) == 0:

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

        return self.words[random.randint(0, len(self.words))].strip()

    def reset_bad_guess_count(self, count):
        self.bad_guesses = count

    def get_new_word(self):
        return self.select_word()

    def reset_game(self):
        import string

        # https://docs.python.org/3/library/string.html#string-constants
        self.available_letters = list(string.ascii_lowercase)

        self.guessed_letters = []

        self.target_word = self.get_new_word()

        # create a set for tracking valid guess, remove a valid guess and check for winning status by checking len
        self.target_letters = set(self.target_word)

        self.reset_bad_guess_count(7)

    # main function
    def run(self):
        display.welcome_menu()

        self.select_menu_option()

if __name__ == "__main__":
    m = Main()
    m.run()

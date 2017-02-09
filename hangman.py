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
        self.start_menu_options = ['Start Game', 'Exit']

        # get line count
        # http://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines/20756176#20756176
        # load line into class words attribute
        with open(self.file_name, "r") as file:
            self.words = file.read().splitlines()

    def start_game(self):

        self.game_loop()

    def game_loop(self):

        game_status = True

        self.reset_game()

        #print(self.target_word)

        display.game_board(self.target_word)

        while game_status:

            # dictionary from: https://www.flocabulary.com/5th-grade-vocabulary-word-list/

            display.guess_letter_message()

            display.available_letters(self.available_letters)

            good_guess = self.get_guess()

            while not good_guess:
                good_guess = self.get_guess()
                break

            if good_guess in self.target_letters:

                self.remove_from_available_letters(good_guess)

                self.guessed_letters.append(good_guess)

                self.target_letters.remove(good_guess)

                display.correct_guessed_letters(self.target_word, self.guessed_letters)

            else:

                self.bad_guesses -= 1

                if self.bad_guesses <= 0:

                    game_status = False

                    print('game over')
                    print('the word was ', self.target_word)

                else:

                    self.remove_from_available_letters(good_guess)

                    print('bad guess. {} guesses remaining'.format(self.bad_guesses))

                    display.correct_guessed_letters(self.target_word, self.guessed_letters)

            if len(self.target_letters) == 0:

                print("You win")

                game_status = False

        # restart game

        self.run()

    # get menu option
    def select_menu_option(self):

        while True:
            selection = input("\n")

            if display.is_valid_menu_option(selection, self.start_menu_options):

                return int(selection)

            else:
                print('not a valid selection')

    # selects random word from words.txt
    def select_word(self):
        import random

        return self.words[random.randint(0, len(self.words))].strip()

    def reset_bad_guess_count(self, count):
        if type(count) is not int:
            try:
                count = int(count)
            except (ValueError, TypeError):
                count = 7

        self.bad_guesses = count

    def get_guess(self):
        return input('\n').lower()

    def remove_from_available_letters(self, guess):
        self.available_letters.remove(guess)

    def is_in_available_letters(self, guess):
        if guess not in self.available_letters:
            print('\nThat\'s not a valid guess.\n')
            return False
        else:
            return guess

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

        display.welcome_message()

        display.menu(self.start_menu_options)

        selection = self.select_menu_option()

        if selection == 0:

            self.start_game()

        elif selection == 1:

            exit()

if __name__ == "__main__":
    m = Main()
    m.run()

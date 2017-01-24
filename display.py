class Display:

    @staticmethod
    def welcome_menu():
        print("Welcome to Hangman")
        print("Press 1 to start, 2 to exit")

    @staticmethod
    def show_game_board(word):

        empty_word_string = ''

        for i in word:

            empty_word_string += '_ '

        print("\n" + empty_word_string)

        pass

    @staticmethod
    def guess_letter_message():
        print("\nGuess a letter")

    @staticmethod
    def show_available_letters(available_letters, guessed_letters):
        print('\n\t\t\t\tAvailable letters')
        print(' '.join(available_letters))



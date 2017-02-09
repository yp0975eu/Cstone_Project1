def welcome_menu():
    print("Welcome to Hangman")
    print("Press 1 to start, 2 to exit")


def game_board(word):
    empty_word_string = ''

    for i in word:

        empty_word_string += '_ '

    print("\n" + empty_word_string.strip())


def guess_letter_message():
    print("\nGuess a letter")


def available_letters(letters):
    print('\n\t\t\t\tAvailable letters')
    print(' '.join(letters))


def show_word(word):
    print(word)


def correct_guessed_letters(word, guessed_letters):
    guess_string = ''

    for letter in word:
        if letter in guessed_letters:
            guess_string += ' ' + letter + ' '
        else:
            guess_string += '_ '

    # remove leading and trailing white space
    print(guess_string.strip())

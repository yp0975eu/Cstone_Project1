def welcome_message():
    print("Welcome to Hangman")


def menu(menu_options):
    for i, menu_option in enumerate(menu_options):
            print("Press {} to {}".format(i, menu_option))


def is_valid_menu_option(selection, menu_list=list):
    try:
        selection_int = int(selection)
        if selection_int < 0:
            return False
        # if the index is in the list then nothing will happen, and return true.
        #  if it is not in list then an exception is raised and return false.
        menu_list[selection_int]
        return True
    except (ValueError, IndexError):
        return False


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
            guess_string += letter + ' '
        else:
            guess_string += '_ '

    # remove leading and trailing white space
    print(guess_string.strip())

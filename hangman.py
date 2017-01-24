import display


def start_game():

    # dictionary from: https://www.flocabulary.com/5th-grade-vocabulary-word-list/
    word = select_word()

    display.Display.show_game_board(word)


# get menu option
def select_menu_option():

    selection = input("\n")

    while selection not in ['1', '2']:

        selection = input("\n")

    if selection == '1':

        start_game()

    elif selection == '2':

        exit()


# selects random word from words.txt
def select_word():
    import random
    i = 0

    file_name = 'words.txt'

    # get line count
    # http://stackoverflow.com/q/845058
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass

    file = open(file_name, "r")

    lines = file.readlines()

    return lines[random.randint(0, i)]


# main function
def run():
    display.Display.welcome_menu()
    select_menu_option()

if __name__ == "__main__":
    run()

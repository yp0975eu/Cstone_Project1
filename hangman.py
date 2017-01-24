
def select_word():
    import random
    i = 0

    file_name = '/usr/share/dict/words'

    # get line count
    # http://stackoverflow.com/q/845058
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass

    file = open(file_name, "r")

    lines = file.readlines()
    return lines[random.randint(0, i)]


def run():
    target_word = select_word()
    print("Welcome to Hangman")
    print("Word: ", target_word)

if __name__ == "__main__":
    run()

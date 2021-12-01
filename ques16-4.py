def do_2ice(f, word):
    f(word)
    f(word)


def print_2ice(string):
    print(string)
    print(string)


newWord = "spam"
do_2ice(print_2ice, newWord)

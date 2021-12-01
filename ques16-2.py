word = str(input('What word to repeat?\n'))


def do_twice(f, word):
    f(word)
    f(word)


def print_spam(word):
    print(word)


do_twice(print_spam, word)

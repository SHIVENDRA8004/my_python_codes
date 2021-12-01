def do_twice(f):
    f()
    f()


def print_spam():
    print('Advanced Programming')


do_twice(print_spam)

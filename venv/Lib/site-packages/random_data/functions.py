import random


def random_element(_list):
    secure_random = random.SystemRandom()
    return secure_random.choice(_list)


def list_in_string(_string, _list):
    response = False

    for i in _list:
        if i in _string:
            response = True
            break

    return response
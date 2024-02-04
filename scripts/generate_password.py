#!/usr/bin/python

import random
import string
import sys

characters = string.ascii_letters + string.digits + string.punctuation

def generate_password(length):
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
    else:
        length = 16

    print(generate_password(length))


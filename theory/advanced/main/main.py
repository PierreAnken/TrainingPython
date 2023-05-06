print('I\'m before the main')


if __name__ == '__main__':
    print('I was called from my own path')
else:
    print('I was imported from', __name__)

print('I\'m after the main')


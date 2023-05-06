import time
from datetime import datetime
from itertools import cycle


def get_short_time():
    return str(datetime.now().time())[:8]


if __name__ == '__main__':

    colors = ['Red', 'Green', 'Yellow']

    for color in cycle(colors):
        print(f'{get_short_time()} {color}')
        time.sleep(2)

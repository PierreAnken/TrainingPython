import time
from datetime import datetime


def get_short_time():
    return str(datetime.now().time())[:8]


def get_next_color(previous_color: str):
    if previous_color == 'Red':
        return 'Green'
    elif previous_color == 'Green':
        return 'Yellow'
    else:
        return 'Red'


if __name__ == '__main__':
    current_color = 'Red'

    while True:
        current_color = get_next_color(current_color)
        print(f'{get_short_time()} {current_color}')
        time.sleep(2)

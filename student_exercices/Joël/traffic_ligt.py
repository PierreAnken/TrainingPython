import itertools
import time

if __name__ == '__main__':

    colors = {'red': 2, 'green': 3, 'yellow': 1}

    color_name_cycle = itertools.cycle(colors)  # ['red', 'green', 'yellow']

    for color_name in color_name_cycle:
        color_time = colors[color_name]
        time.sleep(color_time)
        print(color_name)

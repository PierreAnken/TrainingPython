import os

if __name__ == '__main__':

    # create folder calendar if not already existing
    if not os.path.exists('calendar'):
        os.mkdir(path='calendar')

    for month_number in range(1, 13):
        if not os.path.exists(f'calendar/{month_number}'):
            os.mkdir(path=f'calendar/{month_number}')

        for day_number in range(1, 31):
            with open(f'calendar/{month_number}/{day_number}.txt', 'w'):
                pass

    for root, dirs, files in os.walk("calendar", topdown=True):
        print(root, dirs, files)


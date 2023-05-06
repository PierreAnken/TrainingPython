import os
import time

if __name__ == '__main__':

    # create folder data in current folder
    # only if not already existing
    if not os.path.exists('data'):
        os.mkdir(path='data')

    time.sleep(10)

    # delete folder data from current folder
    os.rmdir(path='data')


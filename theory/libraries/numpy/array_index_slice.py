import numpy as np

if __name__ == '__main__':

    # The difference with multidimensional list is the way of accessing sub-dimension

    list_2d = [[1, 2], [3, 4]]
    print('2-dimensional list:', list_2d)
    print('Access [1][1]:', list_2d[1][1])

    array_2d = np.array([[1, 2], [3, 4]])
    print('\n2-dimensional ndarray:\n', array_2d)
    print('Access [1,1]:', array_2d[1, 1])

    # Like with lists, you can use negative indexes
    print('Access [-1,-1]:', array_2d[-1, -1])

import numpy as np

if __name__ == '__main__':
    # NumPy works with ndarray (array) objects
    array = np.array([1, 2, 3, 4, 5])
    print('Basic array:', array)

    # Dimensions
    array_0d = np.array(5)
    print(array_0d.ndim, 'dimension(s) array:', array_0d)

    array_1d = np.array([1, 2, 3, 4, 5])
    print(array_1d.ndim, 'dimension(s) array:', array_1d)

    array_2d = np.array([[1, 2], [3, 4]])
    print(array_2d.ndim, 'dimension(s) array:', '\n', array_2d)

    array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
    print(array_3d.ndim, 'dimension(s) array:', '\n', array_3d)

    # x dimensions on init
    array_xd = np.array(1, ndmin=5)
    print(array_xd.ndim, 'dimension(s) array:', '\n', array_xd)

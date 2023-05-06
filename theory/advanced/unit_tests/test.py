import unittest

from my_functions import get_first_element_from_list


class TestGetFirstElementFromList(unittest.TestCase):
    def test_get_first_element_from_list(self):
        """
        Test that the function return the first element or None if empty
        """

        test_datas_results = [
            ([1, 2, 3], 1),
            ([2, 3], 2),
            ([1], 1),
            (None, None),
            ([False], False),
            (False, None),
        ]

        for test, result in test_datas_results:
            self.assertEqual(get_first_element_from_list(test), result)


if __name__ == '__main__':
    unittest.main()
    # python -m unittest test (in the current folder)

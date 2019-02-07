# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on


def reverselist(lst):
    new_lst = lst[::-1]
    return new_lst
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase


class reverselistTest(unittest.TestCase):
    # each method in this class is a test to be run
    def testOne(self):
        self.assertEqual(reverselist(['a', 'b', 'c', 'd']), [
                         'd', 'c', 'b', 'a'])

    def testTwo(self):
        self.assertEqual(reverselist([1, 2, 3, 4]), [4, 3, 2, 1])

    def testThree(self):
        self.assertEqual(reverselist([0, 'a', 'b']), ['b', 'a', 0])

    def setUp(self):
        pass
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()  # this runs our tests

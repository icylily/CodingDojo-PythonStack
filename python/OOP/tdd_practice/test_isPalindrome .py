# import the python testing framework
import unittest

def isPalindrome(str):
   
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


class isPalindromeTest(unittest.TestCase):
    # each method in this class is a test to be run
    def testOne(self):
        self.assertEqual(isPalindrome("abcde"), False)
    def testTwo(self):
        self.assertEqual(isPalindrome("racecar"), True)

    def testThree(self):
        self.assertTrue(isPalindrome("racecar"))

    def testFour(self):
        self.assertFalse(isPalindrome("123dec"))

    def testFive(self):
        self.assertTrue(isPalindrome("12a21"))
                

    def setUp(self):
        pass
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method

    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()  # this runs our tests


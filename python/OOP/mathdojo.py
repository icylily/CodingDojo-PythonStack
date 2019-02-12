import unittest

class MathDojo:
    def __init__(self):
    	self.result = 0

    def add(self, num, *nums):
    	# your code here
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):

    	# your code here
        self.result -= num
        for n in nums:
            self.result -= n
        return self
        # create an instance:
# md = MathDojo()
# # to test:
# x = md.add(2).add(2, 5, 1).subtract(3, 2).result
# print(x)  # should print 5
# # run each of the methods a few more times and check the result!


class MathDojoTest(unittest.TestCase):
    # each method in this class is a test to be run
    def setUp(self):
        # md = MathDojo()
        # add the setUp tasks
        print("running setUp")
    def testOne(self):
        md = MathDojo()
        self.assertEqual(md.add(2).result,2)

    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.add(2).add(2,3,4).result, 11)
    

    def testThree(self):
        md = MathDojo()
        self.assertEqual(md.subtract(0).result, 0)
    def testsFour(self):
        md = MathDojo()
        self.assertEqual(md.subtract(0).subtract(2,3).result,-5)
    
    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()  # this runs our tests

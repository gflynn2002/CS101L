########################################################################
##
## CS 101 Lab
## Inheritence
## Gabriel Flynn
## gflynn2002@gmail.com
##
## Test a total average and median functions to make sure they work properly
##  
## ERROR HANDLING:
##      No errors found.
##
## OTHER COMMENTS:
##      No other comments.
##
########################################################################


import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):

    def test_total_returns_total_of_list(self):
        values = [1,10,22]
        result = Grades.total(values)
        self.assertEqual(result,33,'The total function should return 33')
    
    def test_total_returns_0(self):
        values = []
        result = Grades.total(values)
        self.assertEqual(result,0, 'The total function should return 0')
    
    def test_average_one(self):
        values = [2,5,9]
        result = Grades.average(values)
        self.assertAlmostEqual(result, 5.33333, 5, 'The total function should return 5.33333')

    def test_average_two(self):
        values = [2,15,22,9]
        result = Grades.average(values)
        self.assertAlmostEqual(result, 12.00000,5,'The total function should return 12.00000')

    def test_average_returns_nan(self):
        values = []
        result = Grades.average(values)
        self.assertIs(result, math.nan, 'The total function should return math.nan') 

    def test_median_three(self):
        values = [2,5,1]
        result = Grades.median(values)
        self.assertEqual(result,2,'The total function should return 2')

    def test_median_four(self):
        values = [5,2,1,3]
        result = Grades.median(values)
        self.assertEqual(result,2.5,'The total function should return 2')

    def test_median_valueerror(self):
        values = []
        with self.assertRaises(ValueError):
            result = Grades.median(values)
        
unittest.main()

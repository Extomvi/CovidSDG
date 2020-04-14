import unittest
import math
from unittest import TestCase
from estimator import severeImpact


class EstimatorTest(unittest.TestCase):
            
    def test_power(self):
        self.assertEquals(pow(5, 2), 25)

 
if __name__ == '__main__':
    unittest.main()
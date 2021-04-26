import unittest
from compute_stats import *

class Test(unittest.TestCase):
    def test_counten(self):
        self.assertEqual(counten(),1000)

    def test_summan(self):
        self.assertEqual(summan(),499498)

    def test_averagen(self):
        self.assertEqual(averagen(),499498/1000)

    def test_minmaxen(self):
        minen,maxen=minmaxen()
        assert minen==1 and maxen==997

if __name__ == '__main__':
    unittest.TestCase()

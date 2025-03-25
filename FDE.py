import unittest

def sort(width, height, length, mass):
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        return "One or more dimensions is less than or equal to 0, please enter value greater than 0."
    isBulky = False
    isHeavy = False
    bulkLimit = 1000000
    heavyLimit = 20
    if width * height * length >= bulkLimit:
        isBulky = True
    if mass >= heavyLimit:
        isHeavy = True
    if isBulky and isHeavy:
        return "REJECTED"
    elif isBulky or isHeavy:
        return "SPECIAL"
    else:
        return "STANDARD"
    
class TestSortMethod(unittest.TestCase):
    def test_all_zeroes(self):
        self.assertEqual(sort(0,0,0,0), "One or more dimensions is less than or equal to 0, please enter value greater than 0.")
    def test_one_zero(self):
        self.assertEqual(sort(10,10,10,0), "One or more dimensions is less than or equal to 0, please enter value greater than 0.")
    def test_negative(self):
        self.assertEqual(sort(10,10,10,-10), "One or more dimensions is less than or equal to 0, please enter value greater than 0.")
    def test_standard(self):
        self.assertEqual(sort(10,10,10,10), "STANDARD")
    def test_heavy(self):
        self.assertEqual(sort(10,10,10,20), "SPECIAL")
    def test_bulky(self):
        self.assertEqual(sort(100,100,100,10), "SPECIAL")
    def test_rejected(self):
        self.assertEqual(sort(100,100,100,20), "REJECTED")

if __name__ == '__main__':
    unittest.main()
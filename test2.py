import unittest
 
def add_numbers(a, b):
    return a + b
 
 
class TestAddNumbers (unittest.TestCase):
    def test_positive_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
 
 
    def test_negative_numbers(self):
        result = add_numbers(-1, 7)
        self.assertEqual(result, 6)
       
    def test_zero_numbers(self):
        result =add_numbers(0, 0)
        self.assertEqual(result, 0)
       
if __name__ == "__main__":
    unittest.main()
 
 
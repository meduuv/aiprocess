import unittest
from aiprocess import clean,limit
class Tests(unittest.TestCase):
 def test_process(self): self.assertEqual(clean(" a  b "),"a b");self.assertEqual(limit("abcd",2),"ab")
if __name__=="__main__":unittest.main()

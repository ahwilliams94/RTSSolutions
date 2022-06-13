import unittest

from main import Solutions

class TestSolution(unittest.TestCase):

  def testAboveBelow(self):
    test_list1 = [1,2,3,4,5,6,7,8,9,10]
    test_value1 = 5
    return1 = Solutions.aboveBelow(test_list1, test_value1)
    self.assertEquals({"above": 5, "below": 4}, return1)
  
    test_list2 = [0,0,0,0,0,0,0,0,0,0]
    test_value2 = 0
    return2 = Solutions.aboveBelow(test_list2, test_value2)
    self.assertEquals({"above": 0, "below": 0}, return2)
    
    test_list3 = []
    test_value3 = 198
    return3 = Solutions.aboveBelow(test_list3, test_value3)
    self.assertEquals({"above": 0, "below": 0}, return3)
  
    test_list4 = [-12,34,76354,23,-123344,-563,5009,134]
    test_value4 = -1
    return4 = Solutions.aboveBelow(test_list4, test_value4)
    self.assertEquals({"above": 5, "below": 3}, return4)

  def testStringRotation(self):
    test_string1 = "TestString"
    test_value1 = 5
    return1 = Solutions.stringRotation(test_string1, test_value1)
    self.assertEquals("tringTestS", return1)

    test_string2 = "TestString"
    test_value2 = 10
    return2 = Solutions.stringRotation(test_string2, test_value2)
    self.assertEquals("TestString", return2)

    test_string3 = "TestString"
    test_value3 = 405
    return3 = Solutions.stringRotation(test_string3, test_value3)
    self.assertEquals("tringTestS", return3)

if __name__ == '__main__':
    unittest.main()

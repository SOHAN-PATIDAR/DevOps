import unittest

def add(n1,n2):
    """Add two integers"""
    return(n1+n2)

def substract(n1,n2):
    """Substract two integers"""
    return(n1-n2)

def multiply(n1,n2):
    """Multiply two integers"""
    return(n1*n2)

class UnitTest(unittest.TestCase):

    def test_add(self):
        "Test cases for addition"
        self.assertEqual(10,add(0,10))
        self.assertEqual(100,add(36,64))
        self.assertEqual(90,add(33,57))
        self.assertEqual(50,add(23,27))
      
    def test_substract(self):
        "Test cases for sustraction"
        self.assertEqual(50,substract(90,40))
        self.assertEqual(-6,substract(0,6))
        self.assertEqual(15,substract(30,15))
        self.assertEqual(0,substract(100,100))
     
    def test_multiply(self):
        "Test cases for multiplication"
        self.assertEqual(0,multiply(0,1000)) 
        self.assertEqual(100,multiply(10,10)) 
        self.assertEqual(64,multiply(4,16)) 
        self.assertEqual(81,multiply(27,3)) 

unittest.main()
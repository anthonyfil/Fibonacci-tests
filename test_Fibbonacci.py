import unittest
import Fibbonacci
class test_Fibbonacci(unittest.TestCase): 
	def test_Fib(self):
                #Testing Actual Results
		result = Fibbonacci.Fib(1)
		self.assertEqual(result, 1)
		
		result = Fibbonacci.Fib(2)
		self.assertEqual(result, 1)
		
		result = Fibbonacci.Fib(8)
		self.assertEqual(result, 21)
	def test_Fib_negative(self):
                #Testing negatives
		result = Fibbonacci.Fib(-1)
		self.assertEqual(result,  "Error")
		
		result = Fibbonacci.Fib(-5)
		self.assertEqual(result,  "Error")
		result = Fibbonacci.Fib(0)
		self.assertEqual(result, "Error")
	def test_Fib_text(self):
		#Testing text
		result = Fibbonacci.Fib("Words")
		self.assertEqual(result, "Error")
		
		result = Fibbonacci.Fib(["3", "4", "we"])
		self.assertEqual(result, "Error")
	def test_Fib_other(self):
		#testing complex numbers
		result = Fibbonacci.Fib(complex(5,2))
		self.assertEqual(result, "Error")
		
		result = Fibbonacci.Fib([complex(5,2), complex(5,2)])
		self.assertEqual(result, "Error")
		#testing emptly list
		result = Fibbonacci.Fib([])
		self.assertEqual(result, "Error")
		


if __name__ == "__main__":
        unittest.main()

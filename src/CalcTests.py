import unittest, csv
from Calculator import Calculator
from CsvReader import CsvReader
calculator = Calculator()


class KnownValues(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(calculator, Calculator)


    def test_addition_csv(self):
        test_add= CsvReader('src/addition.csv').data
        for row in test_add:
            self.assertEqual(calculator.add(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))


    def test_subtraction_csv(self):
        test_sub= CsvReader('src/subtraction.csv').data
        for row in test_sub:
            self.assertEqual(calculator.subtract(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))


    def test_multiplication_csv(self):
        test_mul= CsvReader('src/multiplication.csv').data
        for row in test_mul:
            self.assertEqual(calculator.multiply(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))

if __name__== '__main__':
    unittest.main()
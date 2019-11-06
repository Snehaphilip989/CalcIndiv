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


    def test_square_csv(self):
        test_sq= CsvReader('src/square.csv').data
        for row in test_sq:
            self.assertEqual(calculator.square(int(row['Value 1'])), int(row['Result']))


    def test_multiplication_csv(self):
        test_mul= CsvReader('src/multiplication.csv').data
        for row in test_mul:
            self.assertEqual(calculator.multiply(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))

    def test_subtraction_csv(self):
        test_sub= CsvReader('src/subtraction.csv').data
        for row in test_sub:
            self.assertEqual(calculator.subtract(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))


    def test_division_csv(self):
        test_div= CsvReader('src/division.csv').data
        for row in test_div:
            result = round(calculator.divide(int(row['Value 2']),int(row['Value 1'])),7)
            self.assertEqual(result, round(float(row['Result']),7))


    def test_squareroot_csv(self):
        test_sqroot= CsvReader('src/root.csv').data
        for row in test_sqroot:
            result = round(calculator.root(int(row['Value 1'])),8)
            self.assertEqual(result, round(float(row['Result']),8))

if __name__== '__main__':
    unittest.main()
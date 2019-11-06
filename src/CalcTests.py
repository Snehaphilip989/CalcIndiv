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


if __name__== '__main__':
    unittest.main()
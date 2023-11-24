import unittest
from io import StringIO
import sys

from src.main import optimal_order


class TestOptimalOrder(unittest.TestCase):

    def test_optimal_order_example1(self):
        input_data = "visa foreignpassport\nvisa hotel\nvisa bankstatement\nbankstatement nationalpassport\nhotel creditcard\ncreditcard nationalpassport\nnationalpassport birthcertificate\nforeignpassport nationalpassport\nforeignpassport militarycertificate\nmilitarycertificate nationalpassport\n"
        expected_output = "birthcertificate\nnationalpassport\nmilitarycertificate\nforeignpassport\ncreditcard\nhotel\nbankstatement\nvisa\n"

        with StringIO(input_data) as input_file, StringIO() as output_file:
            sys.stdin = input_file
            sys.stdout = output_file

            optimal_order('govern.in', 'govern.out')

            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

            output_file.seek(0)
            actual_output = output_file.read()

        self.assertEqual(actual_output, expected_output)

    def test_optimal_order_example2(self):
        input_data = "visa foreignpassport\n"
        expected_output = "foreignpassport\nvisa\n"

        with StringIO(input_data) as input_file, StringIO() as output_file:
            sys.stdin = input_file
            sys.stdout = output_file

            optimal_order('govern.in', 'govern.out')

            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__

            output_file.seek(0)
            actual_output = output_file.read()

        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

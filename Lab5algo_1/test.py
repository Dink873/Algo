import unittest
from io import StringIO
import sys
import os

from src.main import optimal_order

class TestOptimalOrder(unittest.TestCase):

    def test_optimal_order_example1(self):
        input_data = "visa foreignpassport\nvisa hotel\nvisa bankstatement\nbankstatement nationalpassport\nhotel creditcard\ncreditcard nationalpassport\nnationalpassport birthcertificate\nforeignpassport nationalpassport\nforeignpassport militarycertificate\nmilitarycertificate nationalpassport\n"
        expected_output = "birthcertificate\nnationalpassport\nmilitarycertificate\nforeignpassport\ncreditcard\nhotel\nbankstatement\nvisa\n"

        input_file_path = 'test_input.txt'
        output_file_path = 'test_output.txt'

        with open(input_file_path, 'w') as input_file:
            input_file.write(input_data)

        optimal_order(input_file_path, output_file_path)

        with open(output_file_path, 'r') as output_file:
            actual_output = output_file.read()

        os.remove(input_file_path)
        os.remove(output_file_path)

        self.assertCountEqual(actual_output.split('\n'), expected_output.split('\n'))

    def test_optimal_order_example2(self):
        input_data = "visa foreignpassport\n"
        expected_output = "foreignpassport\nvisa\n"

        input_file_path = 'test_input.txt'
        output_file_path = 'test_output.txt'

        with open(input_file_path, 'w') as input_file:
            input_file.write(input_data)

        optimal_order(input_file_path, output_file_path)

        with open(output_file_path, 'r') as output_file:
            actual_output = output_file.read()

        os.remove(input_file_path)
        os.remove(output_file_path)

        self.assertCountEqual(actual_output.split('\n'), expected_output.split('\n'))

if __name__ == '__main__':
    unittest.main()

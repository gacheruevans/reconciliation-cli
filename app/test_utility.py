import unittest
import csv
from app.utility import read_csv_file

class TestCSVFunctions(unittest.TestCase):
    def test_read_csv_file(self):
        csv_filename = 'test_file.csv'
        with open(csv_filename, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Date', 'Amount'])
            writer.writerow(['001', 'John Doe', '2023-01-01', '100.00'])
            writer.writerow(['002', 'Jane Smith', '2023-01-02', '200.50'])
            writer.writerow(['003', 'Robert Brown', '2023-01-03', '300.75'])

        expected_result = [{'ID': '001', 'Name': 'John Doe', 'Date': '2023-01-01', 'Amount': '100.00'}, 
                           {'ID': '002', 'Name': 'Jane Smith', 'Date': '2023-01-02', 'Amount': '200.50'}, 
                           {'ID': '003', 'Name': 'Robert Brown', 'Date': '2023-01-03', 'Amount': '300.75'}]
        result = read_csv_file(csv_filename)
        self.assertEqual(result, expected_result)

    def test_read_csv_file_missing_columns(self):
        csv_filename = 'test_file_missing_columns.csv'
        with open(csv_filename, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Date', 'Amount'])
            writer.writerow(['001', 'John Doe', '2023-01-01', ''])
            writer.writerow(['002', 'Jane Smith', '2023-01-02', '200.50'])
            writer.writerow(['003', 'Robert Brown', '', '300.75'])

        expected_result = [{'ID': '001', 'Name': 'John Doe', 'Date': '2023-01-01', 'Amount': None}, 
                           {'ID': '002', 'Name': 'Jane Smith', 'Date': '2023-01-02', 'Amount': '200.50'}, 
                           {'ID': '003', 'Name': 'Robert Brown', 'Date': None, 'Amount': '300.75'}]
        result = read_csv_file(csv_filename)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
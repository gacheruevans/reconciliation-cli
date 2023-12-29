from unittest.mock import patch

@patch('app.utility.read_csv_file')
def test_import_source_data(self, mock_read_csv_file):
    csv_filename = 'test_source.csv'
    self.reconciler.import_source_data(csv_filename)
    mock_read_csv_file.assert_called_with(csv_filename)

@patch('app.utility.read_csv_file')
def test_import_target_data(self, mock_read_csv_file):
    csv_filename = 'test_target.csv'
    self.reconciler.import_target_data(csv_filename)
    mock_read_csv_file.assert_called_with(csv_filename)

@patch('app.utility.write_csv_file')
def test_compare_data(self, mock_write_csv_file):
    source_data = [{'ID': 1, 'Date': '2021-01-01', 'Amount': 100}, {'ID': 2, 'Date': '2021-01-02', 'Amount': 200}]
    target_data = [{'ID': 1, 'Date': '2021-01-01', 'Amount': 100}, {'ID': 3, 'Date': '2021-01-03', 'Amount': 300}]
    self.reconciler.source = source_data
    self.reconciler.target = target_data
    expected_output = [
        "- Missing in Target:2",
        "- Missing in Source:3",
    ]
    self.reconciler.compare_data()
    mock_write_csv_file.assert_called_with(expected_output)
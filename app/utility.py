import csv
from pathlib import Path


def read_csv_file(csv_filename):
    """Grabs the csv data and creates a dictionary"""

    with open(csv_filename, mode='r')as file:
        data = csv.reader(file)
        # Create a list to store the dictionaries
        dict_list = []
        try:
            # Read the header line
            headers = next(data)

            # Iterate over each row of data
            for row in data:
                # Create a dictionary for the current row
                current_dict = {}

                # Iterate over each item in the row and each header
                for header, item in zip(headers, row):
                    # If the item is an empty string, it means the value is missing
                    if item == '':
                        # You can handle missing values in different ways, for example:
                        # - Use a default value, such as None or 0
                        # - Use a placeholder, such as "N/A" or "Missing"
                        # - Raise an exception to stop the program and let the user know about the missing value
                        # Here, we will use a default value of None
                        current_dict[header] = None
                    else:
                        # If the item is not an empty string, add it to the dictionary with the corresponding header as the key
                        current_dict[header] = item

                 # Add the dictionary to the list
                dict_list.append(current_dict)

        except csv.Error as e:
            print("Error importing", csv_filename, ":\n", e)

        return dict_list


def write_csv_file(data):
    """
    Generates the reconciliation report and writes it out to the root of the project
    """

    with open("outputs/reconciliation_report.csv", "w", newline="")as csv_file:
        csv_writer = csv.writer(csv_file)
        try:
            # field = ["Type","Records Identifier","Field", "Source", "Value", "Target Value"]
            # csv_writer.writerow(field) # Write Header to CSV File

            # Write the header line
            # headers = field
            # csv_writer.writerow(headers)

            # Write the data to for row in data:
            csv_writer.writerow(data)
        except csv.Error as e:
            print("Error importing", data, ":\n", e)


def print_source_path(csv_filename):
    file = Path.cwd() / csv_filename
    print(file)


def print_target_path(csv_filename):
    file = Path.cwd() / csv_filename
    print(file)


def print_output_path():
    file_path = Path.cwd() / "outputs/reconciliation_report.csv"
    print(file_path)

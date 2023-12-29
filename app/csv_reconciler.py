from app.utility import read_csv_file, write_csv_file
from datetime import datetime
import re


class Reconciler:
    def __init__(self):
        self.source = {}
        self.target = {}

    def import_source_data(self, csv_filename: str):
        self.source = read_csv_file(csv_filename)

    def import_target_data(self, csv_filename: str):
        self.target = read_csv_file(csv_filename)

    def compare_data(self):
        """
        Returns the Reconciliated records after comparing the source and target data
            Reconciliation completed:
            - Records missing in target: No
            - Records missing in source: No
            - Records with field discrepancies: No

        Has a Time complexity O(n)
        """

        discrepancies = 0
        count_s = 0
        count_t = 0
        result = []

        source = self.source
        target = self.target

        source_dict = {item['ID']: item for item in source}
        target_dict = {item['ID']: item for item in target}

        # Using set asymetric difference of source and target to get all missing values
        missing_ids = set(source_dict.keys()) - set(target_dict.keys())
        new_ids = set(target_dict.keys()) - set(source_dict.keys())

        print("Reconciliation completed:")
        # Grab any missing id's in Target data
        for missing_id in missing_ids:
            count_s += 1
            in_source = missing_id
            result.append("- Missing in Target:" + str(in_source))
            print("- Records missing in target:", count_s)

        # Grab any missing id's in Source data or new Id's in Target that aren't in source
        for new_id in new_ids:
            count_t += 1
            in_target = new_id
            result.append("- Missing in Source:" + str(in_target))
            print("- Records missing in source:", count_t)

        for id, item1 in source_dict.items():
            if id in target_dict:
                item2 = target_dict[id]
                for key in item1.keys():
                    if key == 'Date':
                        # convert dates to datetime objects before comparison
                        source_date = datetime.strptime(item1[key], '%Y-%m-%d')
                        target_date = datetime.strptime(item2[key], '%Y-%m-%d')

                        if source_date != target_date:
                            result.append("Field Discrepancy: {} {} : {} {}".format(
                                item1['ID'], key, source_date, target_date))
                            discrepancies += 1
                    elif key == 'Amount':
                        # convert amounts to float before comparison
                        source_amount = float(item1[key])
                        target_amount = float(item2[key])

                        if source_amount != target_amount:
                            result.append("Field Discrepancy: {} {} : {} {}".format(
                                item1['ID'], key, source_amount, target_amount))
                            discrepancies += 1
                    else:
                        # for case insensitive comparison, transform to lowercase and remove leading/trailing spaces
                        source_value = re.sub(
                            '^[ ]+|[ ]+$', '', item1[key].lower())
                        target_value = re.sub(
                            '^[ ]+|[ ]+$', '', item2[key].lower())

                        if source_value != target_value:
                            result.append("Field Discrepancy: {} {} : {} {}".format(
                                item1['ID'], key, source_value, target_value))
                            discrepancies += 1

        print("- Records with field discrepancies: {}".format(discrepancies) + "\n")
        # Generate the reconciliation report
        write_csv_file(result)

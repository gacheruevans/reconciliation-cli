import string
from app.csv_reconciler import Reconciler
import argparse

from app.utility import print_output_path, print_source_path, print_target_path


class Runner:
    def run(self):
        """
        Prints a brief intor to the CLI application
        """

        # Initialize CSV Reconciler instance
        server = Reconciler()
        server.import_source_data("source.csv")
        server.import_target_data("target.csv")

        print("\nWelcome to the {}  \n".format("Reconciler CLI Application"))
        print(
            "This is a command line interface for reconciling data between two CSV files.\n")
        print(
            "usage: runner.py [-h] [-o] [-s] [-t] [-r] \n \n"

            "Optional arguments: \n"
            "-h, --help       show this help message and exit \n"
            "-o, --output     show path to reconciliation report \n"
            "-s, --source     show path to source csv file \n"
            "-t, --target     show path to target csv file \n"
            "-r, --reconcile  show results and generate a report \n\n"
        )

        # Initialize
        parser = argparse.ArgumentParser(
            description="Reconciler CLI Application")

        # Adding optional parameters
        parser.add_argument(
            "-o", "--output", action="store_true", help="show path to reconciliation report")
        # parser.add_argument('-o or --output is the path to save the output reconciliation report. \n')

        parser.add_argument(
            "-s", "--source", action="store_true", help="show path to source csv file")

        parser.add_argument(
            "-t", "--target", action="store_true", help="show path to target csv file")

        parser.add_argument(
            "-r", "--reconcile", action="store_true", help="show results and generate a report")

        # Parsing the argument
        args = parser.parse_args()

        if args.output:
            print_output_path()

        if args.reconcile:
            server.compare_data()

        if args.source:
            file = "source.csv"
            print_source_path(file)

        if args.target:
            file = "target.csv"
            print_target_path(file)


if __name__ == "__main__":
    Runner().run()

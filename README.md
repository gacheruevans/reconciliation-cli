## Welcome to the Reconciler CLI Application
Please note that this application assumes you have Python 3 installed on your machine and are comfortable using it in the terminal.

Please note that this application assumes that both input CSVs have headers and are comma-separated values (CSV).
The program takes in two CSV file paths as arguments and outputs the differences between them. 

The comparison is done column by column, so if one CSV has an extra column or different values in a specific column compared to another, it will be
noted accordingly.

# Reconciler-CLI
A simple Command Line Interface (CLI) application written in Python that compares two CSV files and identifies any discrepancies between their columns.

### To run the program.
`python runner.py`

### More options.
```
    usage: runner.py [-h] [-o] [-s] [-t] [-r] 
    
    Optional arguments: 
    -h, --help       show this help message and exit 
    -o, --output     show path to reconciliation report 
    -s, --source     show path to source csv file 
    -t, --target     show path to target csv file 
    -r, --reconcile  show results and generate a report 
```